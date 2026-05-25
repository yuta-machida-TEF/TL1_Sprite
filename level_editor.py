import bpy

#ブレンダーに登録するアドオン情報
bl_info = {
    "name" : "レベルエディタ",
    "author" : "Yuta Machida",
    "version" : (1,0),
    "blender" : (3,3,1),
    "location" : "",
    "description": "レベルエディタ",
    "warning" : "",
    "wiki_url" : "",
    "tracker_url": "",
    "category": "Object"
}

#アドオン有効化時
def register():
    print("レベルエディダが有効化されました。")

#アドオン無効化時コールバック
def unregister():
    print("レベルエディダが無効化されました。")

#テスト実行用コード
if __name__  == "__main__":
    register()