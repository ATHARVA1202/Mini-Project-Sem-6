from difflib import SequenceMatcher

import instaloader


def get_instagram_data(username):
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        # Extract the desired attributes for display
        instagram_data = {
            "Username": username,
            "edge_followed_by": profile.followers,
            "edge_follow": profile.followees,
            "username_length": len(username),
            "username_has_number": int(any(char.isdigit() for char in username)),
            "full_name_has_number": int(any(char.isdigit() for char in profile.full_name)),
            "full_name_length": len(profile.full_name),
            "is_private": int(profile.is_private),
            # "is_joined_recently": int(profile.is_joined_recently),
            # "has_channel": int(profile.has_channel),
            "is_business_account": int(profile.is_business_account),
            # "has_guides": int(profile.has_guides),
            "has_external_url": int(bool(profile.external_url)),
            "is_fake": 0  # instaloaderu would need a method to determine if the account is fake
        }
        similarity_ratio = SequenceMatcher(None, username, profile.full_name).ratio()
        instagram_data["username_full_name_similarity"] = similarity_ratio

        return instagram_data

    except instaloader.ProfileNotExistsException:
        print("Profile with username '{}' does not exist.".format(username))
        return None


# Example usage:
username = "atharvadesai_9"
instagram_data = get_instagram_data(username)
if instagram_data:
    print(instagram_data)