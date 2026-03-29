import boto3
from datetime import datetime, timezone

def get_iam_users():
    iam = boto3.client('iam')
    users = iam.list_users()['Users']
    findings = []

    for user in users:
        username = user['UserName']

        # Check if MFA is enabled
        mfa = iam.list_mfa_devices(UserName=username)['MFADevices']
        has_mfa = len(mfa) > 0

        # Check access key age
        keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']
        old_keys = []
        for key in keys:
            age = (datetime.now(timezone.utc) - key['CreateDate']).days
            if age > 90:
                old_keys.append(key['AccessKeyId'])

        # Check if user has admin access
        attached = iam.list_attached_user_policies(UserName=username)['AttachedPolicies']
        is_admin = any(p['PolicyName'] == 'AdministratorAccess' for p in attached)

        # Last login
        last_used = user.get('PasswordLastUsed', 'Never logged in')

        findings.append({
            'User': username,
            'MFA Enabled': 'YES' if has_mfa else 'NO ⚠️',
            'Admin Access': 'YES ⚠️' if is_admin else 'No',
            'Old Keys': old_keys if old_keys else 'None',
            'Last Login': last_used
        })

    return findings

if __name__ == '__main__':
    print("\n🔐 IAM Security Audit Report")
    print("=" * 50)
    findings = get_iam_users()
    for f in findings:
        print(f"\n👤 User: {f['User']}")
        print(f"   MFA Enabled : {f['MFA Enabled']}")
        print(f"   Admin Access: {f['Admin Access']}")
        print(f"   Old Keys    : {f['Old Keys']}")
        print(f"   Last Login  : {f['Last Login']}")
    print("\n" + "=" * 50)
    print("✅ Audit Complete!")