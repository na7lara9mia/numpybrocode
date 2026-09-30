# Copyright (c) Microsoft Corporation.
# Licensed under the MIT Licen***********ample demonstrating:
1. Access variable group values from Python.
2. Use of Service Principal Name (SPN) with a Secret credential flow.
3. Use the Fabric REST APIs to lookup the workspace ID based on workspace name.
4. Using enable_shortcut_publish feature flag to deploy Lakehouse shortcuts.
5. Using debug log level.
"""

import os
import argparse
import requests
import ast
import json
import base64

from fabric_cicd import (
    FabricWorkspace,
    publish_all_items,
    unpublish_all_orphan_items,
    change_log_level,
    append_feature_flag
)

from azure.identity import ClientSecretCredential


def get_workspace_id(p_ws_name, p_token):
    url = "https://api.fabric.microsoft.com/v1/workspaces"

    headers = {
        "Authorization": f"Bearer {p_token.token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    ws_id = ''

    if response.status_code == 200:
        workspaces = response.json()["value"]

        for workspace in workspaces:
            if workspace["displayName"] == p_ws_name:
                ws_id = workspace["id"]
                return ws_id

        if ws_id == '':
            return f"Error: Workspace {p_ws_name} could not found."

    return f"Error: {response.status_code}, {response.text}"

# ------------------------------------------------------------------
# Feature Flags and Logging
# ------------------------------------------------------------------

append_feature_flag("enable_shortcut_publish")
change_log_level("DEBUG")

# ------------------------------------------------------------------
# Arguments
# ------------------------------------------------------------------

parser = argparse.ArgumentParser(
    description='Process Azure Pipeline arguments.'
)

parser.add_argument(
    '--aztenantid',
    type=str,
    help='tenant ID'
)

parser.add_argument(
    '--azclientid',
    type=str,
    help='SP client ID'
)

parser.add_argument(
    '--azspsecret',
    type=str,
    help='SP secret'
)

parser.add_argument(
    '--target_env',
    type=str,
    help='target environment'
)

parser.add_argument(
    '--items_in_scope',
    type=str,
    help='Defines the item types to be deployed'
)

args = parser.parse_args()

# ------------------------------------------------------------------
# Authentication
# ------------------------------------------------------------------

print("Obtaining token...")

token_credential = ClientSecretCredential(
    client_id=args.azclientid,
    client_secret=args.azspsecret,
    tenant_id=args.aztenantid
)

tgtenv = args.target_env

print(f"Target environment set to {tgtenv}")

workspace_name = "[REC] POC_Integration"

print(f"Obtaining GUID for {workspace_name}")

resource = "https://api.fabric.microsoft.com/"
scope = f"{resource}.default"

print(f"scope set to {scope}")

token = token_credential.get_token(scope)

print(f"token acquired, expires_on={token.expires_on}")

# ------------------------------------------------------------------
# JWT DEBUG
# ------------------------------------------------------------------

print("===== TOKEN DEBUG =====")

try:

    jwt_parts = token.token.split(".")

    if len(jwt_parts) >= 2:

        payload = jwt_parts[1]
        payload += "=" * (-len(payload) % 4)

        claims = json.loads(
            base64.urlsafe_b64decode(payload).decode("utf-8")
        )

        interesting_claims = [
            "aud",
            "appid",
            "azp",
            "tid",
            "idtyp",
            "roles",
            "scp"
        ]

        for claim in interesting_claims:
            print(f"{claim} = {claims.get(claim)}")

    else:
        print("Unexpected JWT format")

except Exception a****:
    print(f"Could not decode JWT: {ex}")

print("=======================")

# ------------------------------------------------------------------
# FABRIC API TEST
# ------------------------------------------------------------------

print("===== FABRIC TEST =====")

try:

    fabric_response = requests.get(
        "https://api.fabric.microsoft.com/v1/workspaces",
        headers={
            "Authorization": f"Bearer {token.token}"
        }
    )

    print(f"Status={fabric_response.status_code}")
    print(f"Response={fabric_response.text}")

except Exception a****:
    print(f"Fabric API test failed: {ex}")

print("=======================")



# ------------------------------------------------------------------
# Workspace Lookup
# ------------------------------------------------------------------

lookup_response = get_workspace_id(
    workspace_name,
    token
)

if lookup_response.startswith("Error"):

    errmsg = (
        f"{lookup_response}. "
        f"Perhaps workspace name is set incorrectly.\n"
        f"workspace_name = {workspace_name}\n"
        f"client_id = {args.azclientid}"
    )

    raise ValueError(errmsg)

wks_id = lookup_response

print(
    f"Workspace ID for {workspace_name} set to {wks_id}"
)

# ------------------------------------------------------------------
# Repository
# ------------------------------------------------------------------

repository_directory = os.environ["BUILD_SOURCESDIRECTORY"]+"/fabric/src"

item_types = args.items_in_scope.strip("[]").split(",")

# ------------------------------------------------------------------
# Fabric Workspace Object
# ------------------------------------------------------------------

target_workspace = FabricWorkspace(
    workspace_id=wks_id,
    environment=tgtenv,
    repository_directory=repository_directory,
    item_type_in_scope=item_types,
    token_credential=token_credential
)

# ------------------------------------------------------------------
# Publish
# ------------------------------------------------------------------

print("Publish branch to workspace...")

publish_all_items(target_workspace)

# ------------------------------------------------------------------
# Cleanup
# ------------------------------------------------------------------

unpublish_all_orphan_items(target_workspace)