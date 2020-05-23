test_text = {
    "content": '''<article class="article" id="mp-editor">
    <!-- 政务处理 -->
          <p data-role="original-title" style="display:none">原标题：全国各地各族人民深切悼念抗击新冠肺炎疫情斗争牺牲烈士和逝世同胞 习近平李克强栗战书汪洋王沪宁赵乐际韩正王岐山 在京出席哀悼活动</p>
                <div id="sohuplayer"></div>
          <p class="video-title">
            <span class="video-ionc"></span>
            全国各地各族人民深切悼念抗击新冠肺炎疫情斗争牺牲烈士和逝世同胞习近平等出席哀悼活动
          </p>
          <!--h5播放器-->
<script type="text/javascript" src="//js.tv.itc.cn/base/plugin/showPlayer.js"></script>
<script type="text/javascript">
    // 前插视频
    showPlayer({
        el: '#sohuplayer',
                    bid:'187669683',
                autoplay: false,
        width:'500',
        height:'300',
        mute: 1,
        disablePlaylist:true,  // h5播放器禁用下一集按钮
        variables: [
            ['showRecommend','0'] // 0时不展示后推荐；默认展示
        ]
    });
</script>
             <p>国旗半垂，举国同悲。4月4日，庚子年清明节，全国各地各族人民深切悼念抗击新冠肺炎疫情斗争牺牲烈士和逝世同胞。</p> 
<p>习近平、李克强、栗战书、汪洋、王沪宁、赵乐际、韩正、王岐山等党和国家领导人在首都北京参加悼念。</p> 
<p>新冠肺炎疫情是新中国成立以来在我国发生的传播速度最快、感染范围最广、防控难度最大的一次重大突发公共卫生事件。在抗击疫情的严峻斗争中，一批医务人员、干部职工、社区工作者因公殉职，许多患者不幸罹难。</p> 
<p>今天，北京天安门、新华门和全国人大常委会、国务院、全国政协、中央军事委员会、最高人民法院、最高人民检察院所在地，全国和驻外使领馆下半旗志哀，全国停止公共娱乐活动，以表达全国各族人民对抗击新冠肺炎疫情斗争牺牲烈士和逝世同胞的深切哀悼。</p> 
<p>中南海怀仁堂前气氛庄严肃穆，门楣上悬挂着黑底白字横幅“深切悼念新冠肺炎疫情牺牲烈士和逝世同胞”。习近平等佩戴白花，来到这里，神情凝重面向国旗肃立。</p> 
<p>10时整，防空警报鸣响，习近平等向新冠肺炎疫情牺牲烈士和逝世同胞默哀。</p> 
<p>3分钟，180秒，哀思充满心间。</p> 
<p>英雄的祖国，英雄的人民，书写了人类历史上可歌可泣的抗疫篇章。</p> 
<p>3分钟，180秒，警报响彻神州。</p> 
<p>这场新冠肺炎疫情防控斗争是中华民族伟大复兴历史征程中又一次前所未有的考验。</p> 
<p>这一刻，湖北、武汉和全国各地，人们静立垂首、万分悲痛。汽车、火车、舰船鸣笛声声、久久回荡。</p> 
<p>英雄走好！今天，大江南北，长城内外，国家以最高的祭奠向英雄哀悼，人民以最深的怀念为英雄送行。</p> 
<p>逝者安息！今天，江水呜咽，山川悲鸣，祖国母亲肝肠寸断，亿万同胞泪飞如雨。</p> 
<p>互联网上、朋友圈中，人们自发参与哀悼活动，追思之情绵绵不绝。</p> 
<p>举国哀悼，是对逝者的尊重与缅怀，也是对生命的关爱与珍视。</p> 
<p>一位武汉市民说，我们不会忘记那些逝去的生命，从悲痛中重振，就是对他们最好的告慰。</p> 
<p>一位援鄂医疗队的“90后”党员说，在磨难中成长、从磨难中奋起，这就是我们从这场战“疫”中汲取的力量。</p> 
<p>慎终追远，这庄严肃穆的仪式，寄托着血浓于水的同胞之情，也昭示着慨然前行的奋发之志。</p> 
<p>逝者安息、生者奋进！</p> 
<p>中共中央政治局委员、中央书记处书记，全国人大常委会副委员长，国务委员，最高人民法院院长，最高人民检察院检察长，全国政协副主席，以及中央军委委员就近在工作地点参加哀悼活动。</p> 
<p>全国各地各族干部群众，香港特别行政区同胞、澳门特别行政区同胞、台湾同胞、海外侨胞以不同形式参加悼念活动。</p> 
<p style="text-align: right;"><span style="font-size: 16px;">（编辑 隋博宇）</span><a href="//www.sohu.com/?strategyid=00001 " target="_blank" title="点击进入搜狐首页" id="backsohucom" style="white-space: nowrap;"><span class="backword"><i class="backsohu"></i>返回搜狐，查看更多</span></a></p>      <!-- 政务账号添加来源标示处理 -->
      <!-- 政务账号添加来源标示处理 -->
      <p data-role="editor-name">责任编辑：<span></span></p>
</article>''',

    "creattime": "2012-03-02 10:10:10"
}

import requests

from Jsonabstract.Json_abstract import Json_abstract

Json_abstract = Json_abstract()

#
key_dict = {
    "tit_key_exp": "json_text['data']['title']",
    "con_key_exp": "json_text['data']['content']",
    "time_key_exp": "json_text['data']['time']"
}
# url = 'http://credit.yinchuan.gov.cn/yccredit/ck/queryHtmlByIds?id=17556&satae=1&menuId=92&pmenuId=84'
url = 'http://www.zhwhg.com/api/article/read?id=1099'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
}

response = requests.get(url, headers=headers)

result = Json_abstract.all_abstract(response.json(), key_exp_dict=key_dict)
print(result)
