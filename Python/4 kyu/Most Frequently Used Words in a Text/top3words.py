import operator
import re


def top_3_words(text):
    
    if not text:
        return []
    
    word_count = {}
    
    for word in re.split("[^a-z']+|\\s", text.lower()):
        if word in word_count.keys():
            word_count[word] += 1
        elif word == "" or word == "'" or word == "'''":
            continue
        else:
            word_count[word] = 1
    
    top_3 = [k for k, v in sorted(word_count.items(),
                                  key=operator.itemgetter(1), reverse=True)[:3]]
    
    return top_3


if __name__ == '__main__':
    print(top_3_words(""))
    print(top_3_words("a a a  b  c c  d d d d  e e e e e"))
    print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
    print(top_3_words("  //wont won't won't "))
    print(top_3_words("  , e   .. "))
    print(top_3_words("  ...  "))
    print(top_3_words("  '  "))
    print(top_3_words("  '''  "))
    print(top_3_words("a a a  b  c c X"))
    print(top_3_words("a a c b b"))
    print(top_3_words(
            "In a village of La Mancha, the name of which I have no desire to "
            "caomind, there lived not long since one of those gentlemen that "
            "keep a lancein the lance-rack, an old buckler, a lean hack, "
            "and a greyhound forcoursing. An olla of rather more beef than "
            "mutton, a salad on mostnights, scraps on Saturdays, lentils on "
            "Fridays, and a pigeon or so extraon Sundays, made away with "
            "three-quarters of his income."))
    print(top_3_words(
            "pzpaVpAjEK!;!PcCEMaGG,?rFH/PcCEMaGG:_ _;rFH, //PcCEMaGG ?-rFH!,"
            "pzpaVpAjEK/PcCEMaGG!, _ pzpaVpAjEK:PcCEMaGG;;?PcCEMaGG;rFH- "
            "PcCEMaGG:/:-rFH!- __rFH!XwscgLb_,_!.rFH ,,"
            ".rFH!.!pzpaVpAjEK;-PcCEMaGG? - "
            "XwscgLb:rFH:pzpaVpAjEK?pzpaVpAjEK;_;rFH:pzpaVpAjEK/-_.rFH?_?? "
            "PcCEMaGG.,__/PcCEMaGG. XwscgLb_!!rFH -/,-rFH!:/?_XwscgLb "
            "_pzpaVpAjEK,_/-rFH pzpaVpAjEK -PcCEMaGG "
            "rFH?_pzpaVpAjEK_pzpaVpAjEK:_.;_pzpaVpAjEK,-_,PcCEMaGG_,"
            "PcCEMaGG.:?/pzpaVpAjEK_?;;.XwscgLb:,_!rFH-/pzpaVpAjEK-?!/ "
            "XwscgLb: / _pzpaVpAjEK_PcCEMaGG-rFH ;rFH.rFH!:?/ rFH?,"
            "?:rFH?//XwscgLb. "
            "-PcCEMaGG?;:?PcCEMaGG:/_pzpaVpAjEK!-!;rFH_XwscgLb :;--PcCEMaGG/ "
            ";rFH?pzpaVpAjEK:/,_XwscgLb.-pzpaVpAjEK!-"))
    print(top_3_words(
            "bhjQkQwHt ,?,.pnvyj_, _.havNJda_:pnvyj/-!;-bhjQkQwHt/?, "
            "ChKQfh.bhjQkQwHt_!UWHpFMuUxG-? -,pnvyj!?;/!bhjQkQwHt_ "
            ".pnvyj?bhjQkQwHt?Ljxp !!FtZzR.,--!FtZzR::./FtZzR,"
            "__mbdCkNaD//;Ljxp/,"
            "OuQWDgRWtd_!havNJda!_/!:pnvyj:?-?bhjQkQwHt._/:?KMsVCY_?bhjQkQwHt"
            "-,_:.pnvyj,_-FtZzR-.:?ChKQfh;bhjQkQwHt?,:ChKQfh,"
            "KMsVCY.-KMsVCY?KMsVCY!:!:bhjQkQwHt!--ChKQfh?bhjQkQwHt./!;pnvyj"
            "-pnvyj/! FtZzR  -_ FtZzR.,_bhjQkQwHt?;KMsVCY.ChKQfh/;KMsVCY- "
            "!/KMsVCY!!bhjQkQwHt!pnvyj -havNJda;:!-bhjQkQwHt "
            ".?/bhjQkQwHt_?_Ljxp;UWHpFMuUxG?_?bhjQkQwHt/bhjQkQwHt:mbdCkNaD"
            "-/-FtZzR/UWHpFMuUxG-mbdCkNaD ;_/:bhjQkQwHt;/_UWHpFMuUxG,,;,"
            ".ChKQfh;,;KMsVCY -Ljxp?_!!bhjQkQwHt-;;:/ChKQfh; - "
            ":ChKQfh/:pnvyj.-KMsVCY_:.FtZzR. ! "
            "ChKQfh.FtZzR_.?!ChKQfh._/bhjQkQwHt;,mbdCkNaD..FtZzR: "
            "pnvyj.!:ChKQfh_/;_;FtZzR:/;!.pnvyj/!;pnvyj.mbdCkNaD,"
            "!-mbdCkNaD-/_mbdCkNaD_.,"
            ".ChKQfh;FtZzR!/:-FtZzR:?pnvyj.;havNJda!;:ChKQfh! ,"
            "bhjQkQwHt?KMsVCY:-ChKQfh-/mbdCkNaD?-pnvyj_; .-bhjQkQwHt "
            "FtZzR//_UWHpFMuUxG/_??ChKQfh,;FtZzR ,.?bhjQkQwHt:; pnvyj?-!, "
            "pnvyj.,/?bhjQkQwHt.---Ljxp;.!-ChKQfh,"
            "?ChKQfh-UWHpFMuUxG!_FtZzR/Ljxp;-?KMsVCY?:-pnvyj _.;ChKQfh;?-, "
            "ChKQfh-havNJda?..!!FtZzR//bhjQkQwHt; .mbdCkNaD.:mbdCkNaD/,"
            "pnvyj;-;;.FtZzR?bhjQkQwHt--:Ljxp!?FtZzR;.ChKQfh ,,bhjQkQwHt_,;;,"
            "pnvyj_-!FtZzR;-;,/pnvyj._?--ChKQfh-///UWHpFMuUxG::  !bhjQkQwHt-: "
            "ChKQfh.mbdCkNaD.-;;.KMsVCY/ChKQfh! .!ChKQfh ChKQfh,,-pnvyj;; "
            ":?havNJda?KMsVCY_ !Ljxp??ChKQfh-::/Ljxp,,"
            "/ChKQfh:/Ljxp:.-FtZzR;?OuQWDgRWtd;ChKQfh?-!-;ChKQfh_,"
            "-/:pnvyj/bhjQkQwHt ;_.UWHpFMuUxG,mbdCkNaD;:/Ljxp/,"
            "?-bhjQkQwHt_/mbdCkNaD-KMsVCY!/"))
    print(top_3_words(
            "ncGCitDAX//:!_XwZeqFKjx-_-:hdEf_XwZeqFKjx-XwZeqFKjx_/vxkjrC "
            "_ncGCitDAX ?!rTE,._?!XwZeqFKjx-_ncGCitDAX ,:!,rIG?_kLlM/,"
            "_?ncGCitDAX. -/:rIG;,kLlM!  -/XSeiuBQ!kLlM_XSeiuBQ rTE?hLO!,"
            "hLO!!yTnp;_?:/yU'HfdR,_;?/XwZeqFKjx..XwZeqFKjx:.!vxkjrC  "
            ";hLO?-XSeiuBQ/-_yU'HfdR?/..-XwZeqFKjx!_.;ncGCitDAX.!yU'HfdR?,"
            "KJey?yU'HfdR:,:!.kLlM_??.yTnp/XwZeqFKjx!-rTE,-_vxkjrC- ,"
            "?.XwZeqFKjx!?_rTE,,yU'HfdR! :_-XwZeqFKjx/XSeiuBQ_rTE  "
            "yU'HfdR?;/ncGCitDAX? ?!kLlM!_ ncGCitDAX?.KJey;!,,"
            "ncGCitDAX!_rTE//.ncGCitDAX??.kLlM! "
            "rTE_!yTnp.XwZeqFKjx_;_!kLlM!;!ncGCitDAX.;?XwZeqFKjx"
            "/-!_ncGCitDAX,,_--yU'HfdR,.!hdEf/XwZeqFKjx_,?yU'HfdR?;: "
            "hdEf.:/kLlM:KJey!/kLlM;?.kLlM_. ,:ncGCitDAX?/.-rTE; "
            "XwZeqFKjx/.XwZeqFKjx?/,;!KJey?XwZeqFKjx _ rIG ?.rIG?;_/rIG?_: "
            "?XwZeqFKjx.XSeiuBQ__kLlM!yU'HfdR_-yU'HfdR. ,"
            "_.ncGCitDAX?.kLlM-?!./yU'HfdR__ "
            "kLlM;-?rIG;/:_ncGCitDAX._.-!XwZeqFKjx_;.yTnp/!kLlM?-/?:XSeiuBQ-,"
            "yU'HfdR_ _;kLlM;:kLlM?_,;?kLlM!?_yTnp !/_XSeiuBQ  -?kLlM_,"
            ".yU'HfdR;/.yU'HfdR:-_!;ncGCitDAX/kLlM?; XSeiuBQ,"
            "XwZeqFKjx!ncGCitDAX_,_hdEf-:kLlM_!,-;rIG/?,.XSeiuBQ,"
            "..!ybvpSfGeuZ  !-hdEf !!?:rTE__ "
            "XSeiuBQ-ncGCitDAX;rIG_?XwZeqFKjx:/ hLO;_/,.XwZeqFKjx; "
            "vxkjrC?/!XwZeqFKjx_;?vxkjrC-!ybvpSfGeuZ;-hdEf:hdEf ;!XwZeqFKjx?! "
            ";;rIG/XwZeqFKjx:/XSeiuBQ;yU'HfdR;XSeiuBQ!XwZeqFKjx "
            "hdEf!;KJey-hdEf-;?/ncGCitDAX:?XSeiuBQ,/,hdEf/,,XwZeqFKjx,"
            "/-vxkjrC;ybvpSfGeuZ??-_XSeiuBQ___rTE-; ?_rIG-;-,ncGCitDAX:;yTnp "
            "-;,?ncGCitDAX?hLO//hdEf;:/XwZeqFKjx!kLlM/XwZeqFKjx?;.?.rTE?: "
            "!kLlM_?rTE kLlM /yU'HfdR.;ybvpSfGeuZ -ncGCitDAX: !kLlM "
            ".!!;kLlM-,yU'HfdR?rTE.!_  vxkjrC./:XwZeqFKjx-vxkjrC.KJey/,"
            "?__kLlM. ?KJey/?/XwZeqFKjx rIG!! "))
