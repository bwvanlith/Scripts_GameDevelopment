import unreal

def replace_material(original, replacement):
    original_asset = unreal.EditorAssetLibrary.load_asset(original)
    replacement_asset = unreal.EditorAssetLibrary.load_asset(replacement)
    unreal.EditorAssetLibrary.consolidate_assets(replacement_asset, [original_asset])
    print("Done! Replaced " + original + " with " + replacement)

# Fill in paths to original and replacement materials - replace /CONTENT/ with /GAME/ and don't add a suffix

print('Place this script in the project root (Above the content folder)\n')
old_material = input('Enter old material path (i.e. /Game/MaterialFolder/MaterialName:')
new_material = input('Enter new material path (i.e. /Game/MaterialFolder/MaterialName:')



replace_material(old_material, new_material)
