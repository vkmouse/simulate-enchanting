from flask import Flask
from flask_cors import CORS
from enchantment_database import createMySQLEnchantmentDatabase

app = Flask(__name__)
CORS(app, resources={r"/.*": {"origins": ["http://localhost/*","https://vkmouse.github.io/*"]}})
db = createMySQLEnchantmentDatabase()

@app.route('/')
def hello_world():
    return '2022/09/12'




db.appendNotice({ 
    'Name': '影子技能屬性箱', 
    'Items': [{ 
        'Name': '---------------固定附加第一欄隨機能力---------------',
        'Count': 0,
        'Value': '', 
        'Memo': '',
        'Type': 1 
    }, { 
        'Name': '對無屬性攻擊的抗性+1~2%',
        'Count': 0,
        'Value': '4.500%',
        'Memo': '',
        'Type': 1
    }, { 
        'Name': '對風屬性攻擊的抗性+1~2%',
        'Count': 0,
        'Value': '4.000%',
        'Memo': '',
        'Type': 1
    }, {
        'Name': '---------------10%追加第二欄隨機能力---------------',
        'Count': 0,
        'Value': '',
        'Memo': '',
        'Type': 1
    }, { 
        'Name': '對風屬性攻擊的抗性+3,5%',
        'Count': 0,
        'Value': '4.250%',
        'Memo': '',
        'Type': 1
    }],  
    'Des': '能賦予影子技能系列的附加能力。 需+5以上限定道具才可使用。(附加能力後保留精煉值)', 
    'Url': 'https://ro.gnjoy.com.tw/notice/notice_view.aspx?id=175452',
    'API': 'https://ro.gnjoy.com.tw/notice/Scroll2/ScrollDetail2.ashx?SN=SkillShadowRanBox_TW&scrollID=1023'
})