# coding:utf-8
"""
author:zhouxuan
@project--file : TWERP -->test.py
2020/2/28 17:11
@Desc:
"""
delay_infos = [['白尧', '2020/05/06', 6], ['白尧', '2020/05/13', 2], ['白尧', '2020/05/15', 5], ['白尧', '2020/05/18', 3],
               ['白尧', '2020/05/19', 3], ['白尧', '2020/05/21', 8], ['白尧', '2020/05/22', 65], ['白尧', '2020/05/25', 3],
               ['白尧', '2020/05/26', 5], ['白尧', '2020/05/28', 2], ['曾钰莹', '2020/05/08', '未打卡'], ['曾钰莹', '2020/05/09', 1],
               ['曾钰莹', '2020/05/11', 1], ['曾钰莹', '2020/05/12', 8], ['曾钰莹', '2020/05/13', 6], ['曾钰莹', '2020/05/25', 13],
               ['陈纲', '2020/05/07', 4], ['陈纲', '2020/05/11', 17], ['陈纲', '2020/05/14', 4], ['陈纲', '2020/05/18', 5],
               ['陈纲', '2020/05/25', 1], ['陈路', '2020/05/11', 6], ['陈路', '2020/05/12', 2], ['陈路', '2020/05/13', 10],
               ['陈路', '2020/05/25', 15], ['陈路', '2020/05/27', 118], ['程升', '2020/05/06', '未打卡'],
               ['程升', '2020/05/07', '未打卡'], ['程升', '2020/05/08', '未打卡'], ['程升', '2020/05/09', '未打卡'],
               ['程升', '2020/05/11', '未打卡'], ['程升', '2020/05/12', '未打卡'], ['程升', '2020/05/13', '未打卡'],
               ['程升', '2020/05/14', '未打卡'], ['程升', '2020/05/15', '未打卡'], ['程升', '2020/05/18', '未打卡'],
               ['程升', '2020/05/19', '未打卡'], ['程升', '2020/05/20', '未打卡'], ['程升', '2020/05/21', '未打卡'],
               ['程升', '2020/05/22', '未打卡'], ['程升', '2020/05/25', '未打卡'], ['程升', '2020/05/26', '未打卡'],
               ['程升', '2020/05/27', '未打卡'], ['邓娟', '2020/05/06', '未打卡'], ['邓娟', '2020/05/07', '未打卡'],
               ['邓娟', '2020/05/08', '未打卡'], ['邓娟', '2020/05/09', 14], ['邓娟', '2020/05/12', 7], ['邓娟', '2020/05/13', 2],
               ['邓娟', '2020/05/15', '未打卡'], ['邓娟', '2020/05/19', 8], ['邓娟', '2020/05/21', '未打卡'],
               ['邓娟', '2020/05/22', 7], ['邓娟', '2020/05/27', 8], ['邓星昌', '2020/05/07', '未打卡'],
               ['邓星昌', '2020/05/28', '未打卡'], ['方家威', '2020/05/13', 46], ['方家威', '2020/05/14', 41],
               ['方家威', '2020/05/15', 52], ['方家威', '2020/05/18', 47], ['方家威', '2020/05/19', 27],
               ['方家威', '2020/05/20', 34], ['方家威', '2020/05/21', 47], ['方家威', '2020/05/22', 71],
               ['方家威', '2020/05/25', 59], ['方家威', '2020/05/26', 48], ['方家威', '2020/05/27', 54],
               ['方家威', '2020/05/28', 48], ['方家威', '2020/05/29', 36], ['高杉', '2020/05/13', 31], ['高杉', '2020/05/14', 5],
               ['高杉', '2020/05/22', 14], ['高杉', '2020/05/28', 8], ['龚柱', '2020/05/12', 1], ['龚柱', '2020/05/15', '未打卡'],
               ['贺圆圆', '2020/05/12', 11], ['贺圆圆', '2020/05/20', 2], ['贺圆圆', '2020/05/28', 1], ['黄春', '2020/05/06', 2],
               ['黄春', '2020/05/07', 13], ['黄春', '2020/05/11', 10], ['黄春', '2020/05/12', 4], ['黄春', '2020/05/15', '未打卡'],
               ['黄春', '2020/05/18', '未打卡'], ['黄春', '2020/05/19', '未打卡'], ['黄春', '2020/05/20', '未打卡'],
               ['黄春', '2020/05/26', 3], ['黄敬', '2020/05/08', 124], ['黄庆坤', '2020/05/13', 19], ['雷杰琼', '2020/05/09', 8],
               ['雷杰琼', '2020/05/22', 10], ['雷杰琼', '2020/05/28', '未打卡'], ['雷杰琼', '2020/05/29', '未打卡'],
               ['李春树', '2020/05/13', 2], ['李春树', '2020/05/14', 4], ['李春树', '2020/05/15', 1],
               ['李华', '2020/05/06', '未打卡'], ['李华', '2020/05/15', 1], ['李华', '2020/05/18', 52], ['李华', '2020/05/19', 41],
               ['李华', '2020/05/21', 35], ['李华', '2020/05/22', 38], ['李华', '2020/05/25', 47], ['李华', '2020/05/26', 48],
               ['李华', '2020/05/27', 36], ['李华', '2020/05/28', 40], ['李华', '2020/05/29', 55], ['李娟', '2020/05/11', 5],
               ['李明', '2020/05/26', 222], ['李兴恩', '2020/05/12', 4], ['李兴恩', '2020/05/14', 4], ['李兴恩', '2020/05/15', 25],
               ['李兴恩', '2020/05/18', 3], ['李兴恩', '2020/05/19', 18], ['李兴恩', '2020/05/20', 7], ['李兴恩', '2020/05/21', 28],
               ['李兴恩', '2020/05/22', 48], ['李兴恩', '2020/05/25', 32], ['李兴恩', '2020/05/26', 30],
               ['李兴恩', '2020/05/27', 23], ['李兴恩', '2020/05/28', 44], ['李兴恩', '2020/05/29', 35],
               ['梁柳棋', '2020/05/11', '未打卡'], ['梁柳棋', '2020/05/12', 13], ['梁柳棋', '2020/05/18', 9],
               ['梁柳棋', '2020/05/25', 2], ['刘文兵', '2020/05/13', 11], ['刘文兵', '2020/05/22', '未打卡'],
               ['刘玺', '2020/05/06', 5], ['楼阳生', '2020/05/06', '未打卡'], ['楼阳生', '2020/05/07', '未打卡'],
               ['楼阳生', '2020/05/08', '未打卡'], ['楼阳生', '2020/05/09', '未打卡'], ['楼阳生', '2020/05/11', '未打卡'],
               ['楼阳生', '2020/05/12', '未打卡'], ['楼阳生', '2020/05/13', '未打卡'], ['楼阳生', '2020/05/14', '未打卡'],
               ['楼阳生', '2020/05/15', '未打卡'], ['楼阳生', '2020/05/18', '未打卡'], ['楼阳生', '2020/05/19', '未打卡'],
               ['楼阳生', '2020/05/20', '未打卡'], ['楼阳生', '2020/05/21', '未打卡'], ['楼阳生', '2020/05/22', '未打卡'],
               ['楼阳生', '2020/05/25', '未打卡'], ['楼阳生', '2020/05/26', '未打卡'], ['楼阳生', '2020/05/27', '未打卡'],
               ['楼阳生', '2020/05/28', '未打卡'], ['楼阳生', '2020/05/29', '未打卡'], ['罗甘', '2020/05/09', '未打卡'],
               ['彭哲', '2020/05/06', 247], ['彭哲', '2020/05/15', 1], ['皮碧文', '2020/05/25', '未打卡'],
               ['皮碧文', '2020/05/26', '未打卡'], ['皮碧文', '2020/05/27', '未打卡'], ['皮碧文', '2020/05/28', '未打卡'],
               ['皮碧文', '2020/05/29', '未打卡'], ['邱科', '2020/05/12', 28], ['邱科', '2020/05/15', 2],
               ['邱科', '2020/05/22', 12], ['邱科', '2020/05/26', 19], ['邱科', '2020/05/27', 1], ['邱科', '2020/05/28', 4],
               ['施曼', '2020/05/08', '未打卡'], ['施曼', '2020/05/09', '未打卡'], ['施曼', '2020/05/11', '未打卡'],
               ['施曼', '2020/05/12', '未打卡'], ['施曼', '2020/05/13', '未打卡'], ['施曼', '2020/05/14', '未打卡'],
               ['施曼', '2020/05/15', '未打卡'], ['施曼', '2020/05/18', '未打卡'], ['施曼', '2020/05/19', '未打卡'],
               ['施曼', '2020/05/20', '未打卡'], ['施曼', '2020/05/21', '未打卡'], ['施曼', '2020/05/22', '未打卡'],
               ['施曼', '2020/05/25', '未打卡'], ['施曼', '2020/05/26', '未打卡'], ['施曼', '2020/05/27', '未打卡'],
               ['施曼', '2020/05/28', '未打卡'], ['施曼', '2020/05/29', '未打卡'], ['孙嘉', '2020/05/06', 7],
               ['孙嘉', '2020/05/07', 4], ['孙嘉', '2020/05/09', 17], ['孙嘉', '2020/05/11', 16], ['孙嘉', '2020/05/12', 6],
               ['孙嘉', '2020/05/14', 4], ['孙嘉', '2020/05/15', 2], ['孙嘉', '2020/05/18', 1], ['孙嘉', '2020/05/19', 9],
               ['孙嘉', '2020/05/22', 12], ['孙嘉', '2020/05/25', 7], ['孙权', '2020/05/15', 5], ['孙权', '2020/05/19', 3],
               ['孙权', '2020/05/25', 3], ['田野', '2020/05/11', 2], ['田野', '2020/05/12', 1], ['田野', '2020/05/13', 17],
               ['田野', '2020/05/18', 5], ['田野', '2020/05/25', 14], ['王胜兰', '2020/05/13', 11], ['王胜兰', '2020/05/15', 5],
               ['王胜兰', '2020/05/25', 5], ['王胜兰', '2020/05/26', 3], ['王廷武', '2020/05/06', 3], ['王廷武', '2020/05/07', 3],
               ['王廷武', '2020/05/15', 10], ['王廷武', '2020/05/18', 4], ['王廷武', '2020/05/21', 2],
               ['王廷武', '2020/05/22', '未打卡'], ['王廷武', '2020/05/25', 11], ['王廷武', '2020/05/27', 1],
               ['王廷武', '2020/05/28', 4], ['王玉清', '2020/05/09', '未打卡'], ['王玉清', '2020/05/18', 288],
               ['王政', '2020/05/06', 19], ['王政', '2020/05/07', 3], ['王政', '2020/05/08', 5], ['王政', '2020/05/09', 9],
               ['王政', '2020/05/11', 6], ['王政', '2020/05/12', 10], ['王政', '2020/05/13', 7], ['王政', '2020/05/15', 1],
               ['王政', '2020/05/19', 3], ['王政', '2020/05/20', 1], ['王政', '2020/05/21', 6], ['王政', '2020/05/22', 8],
               ['王政', '2020/05/25', 18], ['王政', '2020/05/26', 12], ['王政', '2020/05/27', 10], ['王政', '2020/05/28', 4],
               ['王志强', '2020/05/06', 21], ['王志强', '2020/05/07', 18], ['王志强', '2020/05/08', 15],
               ['王志强', '2020/05/09', '未打卡'], ['王志强', '2020/05/11', '未打卡'], ['王志强', '2020/05/12', '未打卡'],
               ['王志强', '2020/05/13', 25], ['王志强', '2020/05/14', 18], ['王志强', '2020/05/15', '未打卡'],
               ['王志强', '2020/05/18', 5], ['王志强', '2020/05/19', 20], ['王志强', '2020/05/20', '未打卡'],
               ['王志强', '2020/05/21', 14], ['王志强', '2020/05/22', '未打卡'], ['王志强', '2020/05/25', '未打卡'],
               ['王志强', '2020/05/26', 34], ['王志强', '2020/05/27', 33], ['王志强', '2020/05/28', 22],
               ['王志强', '2020/05/29', 6], ['邬海翔', '2020/05/06', 17], ['邬海翔', '2020/05/08', 1],
               ['邬海翔', '2020/05/11', 255], ['邬海翔', '2020/05/12', 15], ['邬海翔', '2020/05/13', 9],
               ['邬海翔', '2020/05/18', 8], ['邬海翔', '2020/05/22', 5], ['邬海翔', '2020/05/25', 15], ['邬海翔', '2020/05/26', 1],
               ['邬海翔', '2020/05/27', 3], ['邬海翔', '2020/05/29', 3], ['吴路浠', '2020/05/27', 21], ['吴路浠', '2020/05/28', 25],
               ['吴路浠', '2020/05/29', 14], ['吴明明', '2020/05/06', '未打卡'], ['吴明明', '2020/05/07', '未打卡'],
               ['吴明明', '2020/05/08', '未打卡'], ['吴明明', '2020/05/09', '未打卡'], ['吴明明', '2020/05/11', '未打卡'],
               ['吴明明', '2020/05/12', '未打卡'], ['吴明明', '2020/05/13', '未打卡'], ['吴明明', '2020/05/14', '未打卡'],
               ['吴明明', '2020/05/15', '未打卡'], ['吴明明', '2020/05/18', '未打卡'], ['吴明明', '2020/05/19', '未打卡'],
               ['吴明明', '2020/05/20', '未打卡'], ['吴明明', '2020/05/21', '未打卡'], ['吴明明', '2020/05/22', '未打卡'],
               ['吴明明', '2020/05/25', '未打卡'], ['吴明明', '2020/05/26', '未打卡'], ['吴明明', '2020/05/27', '未打卡'],
               ['吴明明', '2020/05/28', '未打卡'], ['吴明明', '2020/05/29', '未打卡'], ['伍梓麒', '2020/05/11', 37],
               ['夏浩波', '2020/05/09', 53], ['夏浩波', '2020/05/11', 51], ['夏浩波', '2020/05/12', '未打卡'],
               ['夏浩波', '2020/05/13', 50], ['夏浩波', '2020/05/14', 52], ['夏浩波', '2020/05/15', 50],
               ['夏浩波', '2020/05/18', 51], ['夏浩波', '2020/05/19', 52], ['夏浩波', '2020/05/20', 54],
               ['夏浩波', '2020/05/21', 57], ['夏浩波', '2020/05/22', 59], ['夏浩波', '2020/05/25', 53],
               ['夏浩波', '2020/05/26', 49], ['夏浩波', '2020/05/27', 44], ['夏浩波', '2020/05/28', 51],
               ['夏浩波', '2020/05/29', 51], ['谢谷雨', '2020/05/06', '未打卡'], ['谢谷雨', '2020/05/09', 7],
               ['谢谷雨', '2020/05/11', 5], ['谢谷雨', '2020/05/15', 1], ['谢谷雨', '2020/05/18', 1], ['谢谷雨', '2020/05/21', 11],
               ['谢谷雨', '2020/05/22', 5], ['熊乐', '2020/05/06', 270], ['熊乐', '2020/05/07', 1], ['熊乐', '2020/05/13', 2],
               ['熊乐', '2020/05/18', 31], ['熊乐', '2020/05/19', 29], ['熊乐', '2020/05/22', 5], ['薛健', '2020/05/06', '未打卡'],
               ['薛健', '2020/05/11', 34], ['薛健', '2020/05/13', 3], ['薛健', '2020/05/14', 9], ['薛健', '2020/05/18', 20],
               ['薛健', '2020/05/19', '未打卡'], ['薛健', '2020/05/22', 130], ['薛健', '2020/05/25', '未打卡'],
               ['严绪进', '2020/05/25', 7], ['颜磊杰', '2020/05/07', 4], ['颜磊杰', '2020/05/13', 6], ['颜磊杰', '2020/05/15', 1],
               ['颜磊杰', '2020/05/21', 2], ['颜磊杰', '2020/05/27', 9], ['杨达奇', '2020/05/06', 243],
               ['杨达奇', '2020/05/27', 195], ['杨艳龙', '2020/05/07', 1], ['杨艳龙', '2020/05/11', 40],
               ['杨艳龙', '2020/05/18', 1], ['杨艳龙', '2020/05/20', '未打卡'], ['杨艳龙', '2020/05/22', '未打卡'],
               ['杨艳龙', '2020/05/27', '未打卡'], ['应兵兵', '2020/05/08', 264], ['应兵兵', '2020/05/09', 257],
               ['应兵兵', '2020/05/11', 27], ['应兵兵', '2020/05/20', 263], ['应兵兵', '2020/05/22', 261],
               ['应兵兵', '2020/05/25', 53], ['应兵兵', '2020/05/29', 6], ['喻蓉', '2020/05/15', 2], ['喻蓉', '2020/05/18', 12],
               ['张浩', '2020/05/08', 15], ['张浩', '2020/05/11', 9], ['张浩', '2020/05/18', 15], ['张浩', '2020/05/25', 5],
               ['张世钦', '2020/05/12', 1], ['张世钦', '2020/05/13', 20], ['张世钦', '2020/05/19', '未打卡'],
               ['张伟', '2020/05/07', 1], ['张伟', '2020/05/11', 261], ['张伟', '2020/05/13', 7], ['张伟', '2020/05/14', 10],
               ['张伟', '2020/05/15', 38], ['张伟', '2020/05/18', 12], ['张伟', '2020/05/20', 7], ['张伟', '2020/05/21', 271],
               ['张欣', '2020/05/06', '未打卡'], ['张欣', '2020/05/07', '未打卡'], ['张欣', '2020/05/08', '未打卡'],
               ['张欣', '2020/05/27', 4], ['张严鑫', '2020/05/21', '未打卡'], ['郑迪岸', '2020/05/06', 65],
               ['郑迪岸', '2020/05/07', '未打卡'], ['郑迪岸', '2020/05/08', 52], ['郑迪岸', '2020/05/09', 37],
               ['郑迪岸', '2020/05/11', 54], ['郑迪岸', '2020/05/12', 44], ['郑迪岸', '2020/05/13', 50],
               ['郑迪岸', '2020/05/14', 56], ['郑迪岸', '2020/05/15', 47], ['郑迪岸', '2020/05/18', 284],
               ['郑迪岸', '2020/05/19', 259], ['郑迪岸', '2020/05/20', 244], ['郑迪岸', '2020/05/21', '未打卡'],
               ['郑迪岸', '2020/05/22', 282], ['郑迪岸', '2020/05/25', 52], ['郑迪岸', '2020/05/26', 68],
               ['郑迪岸', '2020/05/27', 68], ['郑迪岸', '2020/05/29', 48], ['钟华', '2020/05/06', '未打卡'],
               ['钟华', '2020/05/09', 17], ['钟华', '2020/05/11', '未打卡'], ['钟华', '2020/05/12', 4],
               ['钟华', '2020/05/18', '未打卡'], ['钟华', '2020/05/20', '未打卡'], ['钟华', '2020/05/22', '未打卡'],
               ['钟华', '2020/05/25', '未打卡'], ['钟华', '2020/05/29', 30], ['钟晓敏', '2020/05/08', 1],
               ['钟晓敏', '2020/05/09', '未打卡'], ['钟晓敏', '2020/05/12', 2], ['钟晓敏', '2020/05/15', 1],
               ['钟晓敏', '2020/05/18', 14], ['钟晓敏', '2020/05/19', 4], ['钟晓敏', '2020/05/29', 2], ['周玄', '2020/05/14', 10],
               ['朱玲', '2020/05/11', 1], ['朱玲', '2020/05/20', '未打卡']]
names=[]
vip_name=['夏浩波','方家威','施曼','李兴恩','李华',"郑迪岸"]

for info in delay_infos:
    if info[0] in vip_name:
        pass
    elif info[0] not in names:
        names.append(info[0])
"不用考核名单"
for name in names:
    delay_count=0
    greater15_count=0
    less15_count=0
    less5_count=0
    unchecking_count=0  #未打卡
    times=0
    for info in delay_infos:
        if name==info[0]:
            delay_time=info[2] #迟到时间
            if type(delay_time)==int:
                delay_count += 1  # 迟到次数+1
                if delay_time>15:
                    greater15_count+=1
                    times+=delay_time

                elif delay_time>5:
                    less15_count+=1
                else:
                    less5_count+=1
            else:
                unchecking_count+=1

    if delay_count>5 or greater15_count>1 or less15_count>3 or unchecking_count>0 :
        print ("姓名:"+name,',迟到次数',delay_count,'超过15分钟',greater15_count,'次，共计,15分钟内',less15_count,'次，5分钟内',less5_count,'次。未打卡',unchecking_count,"次")



