from unittest import TestCase

from mix_bestpractice import mix


class TestMix(TestCase):
    
    def test_mix_001(self):
        self.assertEqual(mix('Are they here', 'yes, they are here'),
                         '2:eeeee/2:yy/=:hh/=:rr')
    
    def test_mix_002(self):
        self.assertEqual(
                mix('looping is fun but dangerous',
                    'less dangerous than coding'),
                '1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg')
    
    def test_mix_003(self):
        self.assertEqual(
                mix(' In many languages', " there's a pair of functions"),
                '1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt')
    
    def test_mix_004(self):
        self.assertEqual(mix('Lords of the Fallen', 'gamekult'),
                         '1:ee/1:ll/1:oo')
    
    def test_mix_005(self):
        self.assertEqual(mix('codewars', 'codewars'), '')
    
    def test_mix_006(self):
        self.assertEqual(
                mix('A generation must confront the looming ', 'codewarrs'),
                '1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr')
    
    def test_mix_007(self):
        self.assertEqual(mix('Xgzcg@fqtmBgbuw1alkj:qdrqVmctl',
                             'DkjqkUtjbs&stzzFfnii6nwsa-enuv'),
                         '1:ggg/1:qqq/2:nnn/2:sss/1:cc/1:ll/1:mm/2:ii/2:jj/2'
                         ':kk/2:zz/=:tt')
    
    def test_mix_008(self):
        self.assertEqual(mix('XarlrNylasHapfkPsfqu:nqso5klmf',
                             'Qbfvk8dviiBumsi$cxwb.nxslAuvea'),
                         '1:aaa/1:fff/1:lll/1:sss/2:iii/2:vvv/1:kk/1:qq/1:rr'
                         '/2:bb/2:uu/2:xx')
    
    def test_mix_009(self):
        self.assertEqual(mix('Vheyf:nshyUvrpyWblrkHvltn-zqcy',
                             'QlbicFtsqx8rbkh;vsom*vrlx7jssm'),
                         '1:yyyy/2:ssss/1:hh/1:nn/2:bb/2:mm/2:xx/=:ll/=:rr'
                         '/=:vv')
    
    def test_mix_010(self):
        self.assertEqual(mix('HsdrrIlanl)gunwIeasqYhkdo5rbbt',
                             'Oedtm-hoog9quvk.moia9hvya;quen'),
                         '1:rrr/2:ooo/1:bb/1:dd/1:ll/1:nn/1:ss/2:ee/2:hh/2:mm'
                         '/2:qq/2:uu/2:vv/=:aa')
    
    def test_mix_011(self):
        self.assertEqual(mix('4mtuyNupht6egav4wsvgMngbxVwgba',
                             'CzcheRoakr:slwkWjmeoXzhni%gxkb'),
                         '1:gggg/2:kkk/1:aa/1:bb/1:tt/1:uu/1:vv/1:ww/2:ee/2'
                         ':hh/2:oo/2:zz')
    
    def test_mix_012(self):
        self.assertEqual(mix('Tspyz9ffrmIafdeDpkml4jautTpssv',
                             '2vfyk)qknn1gxxd3fvkt0smggQsiga'),
                         '2:gggg/1:fff/1:ppp/1:sss/2:kkk/1:aa/1:mm/2:nn/2:vv'
                         '/2:xx')
    
    def test_mix_013(self):
        self.assertEqual(mix('5nmha<swfzSjtwjLhoebLnibdXsqke',
                             '4yttlQtspt%jrxvMnoob/jiun0xiul'),
                         '2:tttt/1:bb/1:ee/1:hh/1:ss/1:ww/2:ii/2:ll/2:oo/2:uu'
                         '/2:xx/=:jj/=:nn')
    
    def test_mix_014(self):
        self.assertEqual(mix('TjtupGxucqKagqn>wzxsTqtav*omyy',
                             '$ikqgHyamt4upmu/nldkOdurc(dtcn'),
                         '1:qqq/2:ddd/2:uuu/1:aa/1:xx/1:yy/2:cc/2:kk/2:mm/2'
                         ':nn/=:tt')
    
    def test_mix_015(self):
        self.assertEqual(mix('LgepoQvypyQiuyr1iifo2oqpgZtmrq',
                             '2asjb>kdjpJwfhu)hmnwQwtxk9fnmx'),
                         '1:iii/1:ooo/1:ppp/1:yyy/2:www/1:gg/1:qq/1:rr/2:ff/2'
                         ':hh/2:jj/2:kk/2:mm/2:nn/2:xx')
    
    def test_mix_016(self):
        self.assertEqual(mix('Mjlty:eadaVpobyOimii3hzclOytln',
                             'OxelfClrgy0ilsjPbpoh6jvjjWyccu'),
                         '2:jjjj/1:iii/1:yyy/=:lll/1:aa/1:tt/2:cc')
    
    def test_mix_017(self):
        self.assertEqual(mix('Cvwgw=wiucZvhbgRhnko9yqss7yedj',
                             'Jhpwz2idwz(wrgj#rxbe>bzew,jwxb'),
                         '2:wwwww/2:bbb/2:zzz/1:gg/1:hh/1:ss/1:vv/1:yy/2:ee/2'
                         ':jj/2:rr/2:xx')
    
    def test_mix_018(self):
        self.assertEqual(mix('#bqumNijfnRsobo0hayr3mbceVatqx',
                             ">ejesKvixt'woab)umroPvwzzFksuy"),
                         '1:bbb/1:aa/1:mm/1:qq/2:ee/2:ss/2:uu/2:vv/2:ww/2:zz'
                         '/=:oo')
    
    def test_mix_019(self):
        self.assertEqual(mix("Vpdaf4lujf(onat3xdvz$pbhf'mswq",
                             '5oxkz#potx$qmlt3jdef+xjxaFefqy'),
                         '2:xxxx/1:fff/1:aa/1:dd/1:pp/2:ee/2:jj/2:oo/2:qq/2:tt')
    
    def test_mix_020(self):
        self.assertEqual(mix('Xzcik.wsiu)drrc:fiwl-ofpyYihpf',
                             'Bmmuw?nyse<lwyaRjlwn8sccrQnamg'),
                         '1:iiii/1:fff/2:mmm/2:nnn/2:www/1:pp/1:rr/2:aa/2:ll'
                         '/2:ss/2:yy/=:cc')
    
    def test_mix_021(self):
        self.assertEqual(mix('7wdcq;uegqRqqoaYlwzfRkowhAazvl',
                             ';antaMsuqe9exha.zaer)maiv.jdfk'),
                         '2:aaaaa/1:qqqq/1:www/2:eee/1:ll/1:oo/1:zz')
    
    def test_mix_022(self):
        self.assertEqual(mix('Casqe;gtdi5eshh%tpgx%pcqcXdoqk',
                             "'zwepXmhpgSregd;owqsHiqvz<eeyg"),
                         '2:eeee/1:qqq/2:ggg/1:cc/1:dd/1:hh/1:ss/1:tt/2:ww/2'
                         ':zz/=:pp')
    
    def test_mix_023(self):
        self.assertEqual(mix('Scxsx>jwxc)piwo6mjrn?ibda@lmta',
                             '0geaa-ndnb-tovu9bogj@knhmZtpsi'),
                         '1:xxx/2:nnn/1:cc/1:ii/1:jj/1:mm/1:ww/2:bb/2:gg/2:oo'
                         '/2:tt/=:aa')
    
    def test_mix_024(self):
        self.assertEqual(mix('Adhvx/tchb)xlvxWwbxs5bfvu)zldz',
                             'NqnqwIjzix0aufb4edib7pcwa@ycxa'),
                         '1:xxxx/1:bbb/1:vvv/2:aaa/1:dd/1:hh/1:ll/1:zz/2:cc/2'
                         ':ii/2:qq/2:ww')
    
    def test_mix_025(self):
        self.assertEqual(mix('Hfiiw4mlgv*bcod&neyl2gejoNagam',
                             "7epjw'wmex,xbbeJorxv0twliXiefo"),
                         '2:eeee/1:ggg/2:www/2:xxx/1:aa/1:ll/1:mm/2:bb/=:ii'
                         '/=:oo')
    
    def test_mix_026(self):
        self.assertEqual(mix('PclrzHseqrHylkgJumos2qfsxPpotv',
                             '#jede2cxtwPuoizQkwky>cyffExstw'),
                         '1:sss/2:www/1:ll/1:oo/1:qq/1:rr/2:cc/2:ee/2:ff/2:kk'
                         '/2:tt/2:xx/2:yy')
    
    def test_mix_027(self):
        self.assertEqual(mix(',jhfx>hiboOngcfRfnaa0czhvLxcxc',
                             'KlexdAerfs7pgxs6rzny@vqus(vdzg'),
                         '1:cccc/1:fff/1:hhh/1:xxx/2:sss/1:aa/1:nn/2:dd/2:ee'
                         '/2:gg/2:rr/2:vv/2:zz')
    
    def test_mix_028(self):
        self.assertEqual(mix('Yeccc?yioyKpvos#qhln7dccqEalna',
                             'KrzaeHbdubSsfwsXsvxgKgshe)emes'),
                         '1:ccccc/2:sssss/2:eeee/1:aa/1:ll/1:nn/1:oo/1:qq/1'
                         ':yy/2:bb/2:gg')
    
    def test_mix_029(self):
        self.assertEqual(mix('PinkpUyvhhZbyvzAimzp-teorKound',
                             ':nnleLszfeDawso%uaoyAqaenMeryd'),
                         '2:eeee/2:aaa/2:nnn/1:hh/1:ii/1:pp/1:vv/1:zz/2:ss'
                         '/=:oo/=:yy')
    
    def test_mix_030(self):
        self.assertEqual(mix('LicfnPblax9dfhm9bwvo2wyuk0cwux',
                             "Jqlua'nfddQaxkb?eelt&xqivTqyzj"),
                         '1:www/2:qqq/1:bb/1:cc/1:ff/1:uu/2:aa/2:dd/2:ee/2:ll'
                         '/=:xx')
    
    def test_mix_031(self):
        self.assertEqual(mix('Egtln.baib<tenx1jtra:ejfu9hvbx',
                             ';ligdQhdupXiblu+ebtp:ojto4uliu'),
                         '2:uuuu/1:bbb/1:ttt/2:iii/2:lll/1:aa/1:ee/1:jj/1:nn'
                         '/1:xx/2:dd/2:oo/2:pp')
    
    def test_mix_032(self):
        self.assertEqual(mix('Yrorj)hoelCpngp(jkvw2lgkw/saoj',
                             'KhtisQclae;imhs2pvqrMauxx0xbzj'),
                         '1:jjj/1:ooo/2:xxx/1:gg/1:kk/1:ll/1:pp/1:rr/1:ww/2'
                         ':aa/2:hh/2:ii/2:ss')
    
    def test_mix_033(self):
        self.assertEqual(mix('Xoxks&mklp-rqrn/rvyrVscgz#legz',
                             '&oyfm<fsgyIvnbn(zrvqFnbis/kbdo'),
                         '1:rrrr/2:bbb/2:nnn/1:gg/1:kk/1:ll/1:zz/2:ff/2:oo/2'
                         ':vv/2:yy/=:ss')
    
    def test_mix_034(self):
        self.assertEqual(mix('7nhtn<enivRdxqy(khofHjoby&bazq',
                             "9nhpxUdmva:onlz'unxu1ciuv+qzvg"),
                         '2:uuu/2:vvv/=:nnn/1:bb/1:hh/1:oo/1:qq/1:yy/2:xx/2:zz')
    
    def test_mix_035(self):
        self.assertEqual(mix("RcoxlRzjjmWmqaf'cvcsDzlxxMbres",
                             '4anwx,xxko*wgxcEfzot;rzio1ruvi'),
                         '2:xxxx/1:ccc/2:ooo/1:jj/1:ll/1:mm/1:ss/2:ii/2:rr/2'
                         ':ww/=:zz')
    
    def test_mix_036(self):
        self.assertEqual(mix('UhrbpNxngyBlbmf3qbhaJsymj5lofo',
                             '+cctdMiixkLdlwa)fzsv/mawf(tqzu'),
                         '1:bbb/1:hh/1:ll/1:mm/1:oo/1:yy/2:aa/2:cc/2:dd/2:ii'
                         '/2:tt/2:ww/2:zz/=:ff')
    
    def test_mix_037(self):
        self.assertEqual(mix('/fotn&oyas)crfo0rhcbQbdqb.lrbq',
                             '%enjo8xbwzOkbhoPizwy=cvqwYxjzp'),
                         '1:bbbb/1:ooo/1:rrr/2:www/2:zzz/1:cc/1:ff/1:qq/2:jj'
                         '/2:xx')
    
    def test_mix_038(self):
        self.assertEqual(mix('Onvhn>laws:uuyvCtygpJxkdi)nhcx',
                             'Fxzbo=jvfaMqwwqRmfja+kznlPcqpb'),
                         '1:nnn/2:qqq/1:hh/1:uu/1:vv/1:xx/1:yy/2:aa/2:bb/2:ff'
                         '/2:jj/2:ww/2:zz')
    
    def test_mix_039(self):
        self.assertEqual(mix('1nwqs*ekua3ggza2doyvWojwh6sggu',
                             'Dhtxm,rayhPnztwXljmuFvnug=udgb'),
                         '1:gggg/2:uuu/1:aa/1:oo/1:ss/1:ww/2:hh/2:mm/2:nn/2:tt')
    
    def test_mix_040(self):
        self.assertEqual(mix('2sznw7ccavThajf(fmvc<abie*ufhj',
                             'Mfpsa>wfcpIgndl+flkl5nyipKyzmn'),
                         '1:aaa/1:ccc/2:lll/2:nnn/2:ppp/=:fff/1:hh/1:jj/1:vv'
                         '/2:yy')
    
    def test_mix_041(self):
        self.assertEqual(mix('*vzifRstduWzugj,eetk0cnmpFwzke',
                             ';xnwdSzyym@djnk*tjoi@izal@udlo'),
                         '1:eee/1:zzz/2:ddd/1:kk/1:tt/1:uu/2:ii/2:jj/2:ll/2'
                         ':nn/2:oo/2:yy')
    
    def test_mix_042(self):
        self.assertEqual(mix("5zphfQxycs'dayd,alet?itycJgihg",
                             'NcbtyHuexuAreao-msdw1ediz*lpso'),
                         '1:yyy/2:eee/1:aa/1:cc/1:gg/1:hh/1:ii/1:tt/2:oo/2:ss'
                         '/2:uu/=:dd')
    
    def test_mix_043(self):
        self.assertEqual(mix('Llzdm4pnbw=vljy9cqrz<yfeb*wzhc',
                             '9iavmEfzyjNsjjfXlyyg-qawqXoayh'),
                         '2:yyyy/1:zzz/2:aaa/2:jjj/1:bb/1:cc/1:ll/1:ww/2:ff/2'
                         ':qq')
    
    def test_mix_044(self):
        self.assertEqual(mix('(pwyc9lswx)gexhIwjceDwrsx1loif',
                             ';srku/rqwwDzwotVrdayItmyr;issm'),
                         '1:wwww/2:rrrr/1:xxx/2:sss/1:cc/1:ee/1:ll/2:mm/2:tt'
                         '/2:yy')
    
    def test_mix_045(self):
        self.assertEqual(mix('?edabScxjd/khffBandt-cfhi@ejtz',
                             'XcheoXiuik<wwjn-idcr8cvybPoxtm'),
                         '1:ddd/1:fff/2:ccc/2:iii/1:aa/1:ee/1:hh/1:jj/1:tt/2'
                         ':oo/2:ww')
    
    def test_mix_046(self):
        self.assertEqual(mix('1ftvy#roqf-wandWjynaLvmra3rrpz',
                             "Zlhrq'ynfr@ropt%tklz7irmdTmmzx"),
                         '=:rrrr/1:aaa/2:mmm/1:ff/1:nn/1:vv/1:yy/2:ll/2:tt/2'
                         ':zz')
    
    def test_mix_047(self):
        self.assertEqual(mix('DdxliTmpowPaefiOzptxVtiww<kihj',
                             '@zlwoHtaxp/yeewNktgi-bimdNnede'),
                         '1:iiii/2:eeee/1:www/1:pp/1:xx/2:dd/=:tt')
    
    def test_mix_048(self):
        self.assertEqual(mix('Hizdv4gubz5wpnd:lsnf>lzwi-fpon',
                             'Hsond(asjy(tptcTgxzcPbkzc)dlix'),
                         '1:nnn/1:zzz/2:ccc/1:ff/1:ii/1:ll/1:pp/1:ww/2:ss/2'
                         ':tt/2:xx/=:dd')
    
    def test_mix_049(self):
        self.assertEqual(mix('Eiatk=xyek>pincQyvtl?gvrzUfeck',
                             ')jayg=grkqUhwocJoldw5nzji0fzup'),
                         '1:kkk/1:cc/1:ee/1:ii/1:tt/1:vv/1:yy/2:gg/2:jj/2:oo'
                         '/2:ww/2:zz')
    
    def test_mix_050(self):
        self.assertEqual(mix('XvicmWiiqu;zaqi@xgypVlazg,ksoe',
                             'Yahpa.ntcbCcnlm(zqca+akgi1kygt'),
                         '1:iiii/2:aaaa/2:ccc/1:qq/1:zz/2:kk/2:nn/2:tt/=:gg')
    
    def test_mix_051(self):
        self.assertEqual(mix('IdkxvTiaga=pxyaPqrzd.lbrn-casm',
                             'Fvpun%ldtlLexvzYgnypMxiyq*nofy'),
                         '1:aaaa/2:nnn/2:yyy/1:dd/1:rr/2:ll/2:pp/2:vv/=:xx')
    
    def test_mix_052(self):
        self.assertEqual(mix('Zynna*cpgt,tpaoIxpwkXohaqNyhlj',
                             '<zapqFmkwx8hnptAfpps;ycvrPrzug'),
                         '2:pppp/1:aaa/1:hh/1:nn/1:oo/1:tt/1:yy/2:rr/2:zz')
    
    def test_mix_053(self):
        self.assertEqual(mix('>mivzMqypm>xvujKugyiXibpxAummf',
                             'Hoerc<xdkk>uwisIjghj=kkyq3drnr'),
                         '1:mmmm/2:kkkk/1:iii/1:uuu/2:rrr/1:pp/1:vv/1:xx/1:yy'
                         '/2:dd/2:jj')
    
    def test_mix_054(self):
        self.assertEqual(mix('6xwdk@ajog$bzmiGggya-scjs8pkmo',
                             'JyrxqZudrjIehvq*mxne-iwbm@gary'),
                         '1:ggg/2:rrr/1:aa/1:jj/1:kk/1:oo/1:ss/2:ee/2:qq/2:xx'
                         '/2:yy/=:mm')
    
    def test_mix_055(self):
        self.assertEqual(mix('RqmizMgkns&wxbn.gidvAkznwKguew',
                             '1rslp<axzvVftkh;pbbcUkdly,lsde'),
                         '1:ggg/1:nnn/1:www/2:lll/1:ii/1:zz/2:bb/2:dd/2:pp/2'
                         ':ss/=:kk')
    
    def test_mix_056(self):
        self.assertEqual(mix('*qfusTrhez6dbxq:wzdd(ibpkSdzie',
                             '/qgioQfyzv4khzl8ffemEuwdsOutha'),
                         '1:dddd/1:zzz/2:fff/1:bb/1:ee/1:ii/1:qq/2:hh/2:uu')
    
    def test_mix_057(self):
        self.assertEqual(mix('.ukkkDrrlu$auog3bzbdWwubsJxzkr',
                             ",kqad?yhpl'eoxm@aghl6abmjHjiyg"),
                         '1:kkkk/1:uuuu/1:bbb/1:rrr/2:aaa/1:zz/2:gg/2:hh/2:jj'
                         '/2:ll/2:mm/2:yy')
    
    def test_mix_058(self):
        self.assertEqual(mix('Zyhsi;stda7lovh6slvtTrdns=puiu',
                             '/oybz$dmsq.cjcbJrnpoQadlpUigqd'),
                         '1:ssss/2:ddd/1:hh/1:ii/1:ll/1:tt/1:uu/1:vv/2:bb/2'
                         ':cc/2:oo/2:pp/2:qq')
    
    def test_mix_059(self):
        self.assertEqual(mix('Bzwgu6reqx;smabYsybuYtubgFxltf',
                             '(ervuBgrqb5mcxeCoxrv#beflQipcn'),
                         '1:bbb/1:uuu/2:eee/2:rrr/1:gg/1:ss/1:tt/2:cc/2:vv'
                         '/=:xx')
    
    def test_mix_060(self):
        self.assertEqual(mix('.lstj8ppbhTgwmeHtnjm-mouoLpjbm',
                             '1qefxVezxiLppgu&pkjw%nykl3ejmj'),
                         '1:mmmm/2:eee/=:jjj/=:ppp/1:bb/1:oo/1:tt/2:kk/2:xx')
    
    def test_mix_061(self):
        self.assertEqual(mix('.sjyzLgnrv2lnopIqbqn4qssa3pbss',
                             '%xbbxBfnnj7lqmaHvqkaKpzer?oebz'),
                         '1:sssss/1:nnn/1:qqq/2:bbb/1:pp/2:aa/2:ee/2:xx/2:zz')
    
    def test_mix_062(self):
        self.assertEqual(mix('XwjfhCjvkz6lhjwIgrzqJoirg8mfnk',
                             'BidyrAvqjc*zegt4jjqvRfzag?glcc'),
                         '2:ccc/2:ggg/=:jjj/1:ff/1:hh/1:kk/1:rr/1:ww/2:qq/2'
                         ':vv/=:zz')
    
    def test_mix_063(self):
        self.assertEqual(mix('Kmqev3ebuk@fbthOdwsr+lihu%qxnw',
                             '&pzbv*zzxlVcixuRrvstIuwnwBmodv'),
                         '2:vvv/2:zzz/1:bb/1:ee/1:hh/1:qq/2:xx/=:uu/=:ww')
    
    def test_mix_064(self):
        self.assertEqual(mix('Wiieq8kruo6qyuv/gioaFfkzj&gvrf',
                             'SlenxWcfpx3hrooUwjthYmaltTespl'),
                         '1:iii/2:lll/1:ff/1:gg/1:kk/1:qq/1:rr/1:uu/1:vv/2:ee'
                         '/2:hh/2:pp/2:tt/2:xx/=:oo')
    
    def test_mix_065(self):
        self.assertEqual(mix("-odqb*kthrToksi'miwpWipoeNolpz",
                             'InveaCehuo(alceMertr*ibshDmkvy'),
                         '1:oooo/2:eeee/1:iii/1:ppp/1:kk/2:aa/2:hh/2:rr/2:vv')
    
    def test_mix_066(self):
        self.assertEqual(mix('$rvfnVuhbl@ufraHpedc&chhk-sxfu',
                             '+mvzg=enbd;xgozEwieaZtism#xekj'),
                         '1:fff/1:hhh/1:uuu/2:eee/1:cc/1:rr/2:gg/2:ii/2:mm/2'
                         ':xx/2:zz')
    
    def test_mix_067(self):
        self.assertEqual(mix('PkwplBobby>jdlvMtnwh%hgrn3vznk',
                             "'yfks8thdu=swzb;gxoqGrgsx<kvas"),
                         '2:ssss/1:nnn/1:bb/1:hh/1:ll/1:vv/1:ww/2:gg/2:xx/=:kk')
    
    def test_mix_068(self):
        self.assertEqual(mix('9xfgcOyezuQlnscQtpzyYwebuRsshh',
                             'Ptuur/yxceQufpq4gvuj%dlql8dull'),
                         '2:uuuuu/2:llll/1:sss/1:cc/1:ee/1:hh/1:yy/1:zz/2:dd'
                         '/2:qq')
    
    def test_mix_069(self):
        self.assertEqual(mix(')qrna3pxewBtzvmRmubo%cbncPsbvs',
                             "9uyeg'csqg-hysvZzifrTcbbo>lmjs"),
                         '1:bbb/2:sss/1:mm/1:nn/1:vv/2:gg/2:yy/=:cc')
    
    def test_mix_070(self):
        self.assertEqual(mix('6dcopKniyaHzwil@eqgjSqdkw>cmvn',
                             'KfdhuIoqwtTozfqQqstg&jcro*mkzc'),
                         '2:ooo/2:qqq/1:dd/1:ii/1:nn/1:ww/2:ff/2:tt/2:zz/=:cc')
    
    def test_mix_071(self):
        self.assertEqual(mix('Wsskg6absh(jqrbWqygv-wxsy&yjwn',
                             'KlbfeOdvjpOvvdx,rdseMksig0lfsy'),
                         '1:ssss/1:yyy/2:ddd/2:vvv/1:bb/1:gg/1:jj/1:qq/1:ww/2'
                         ':ee/2:ff/2:ll')
    
    def test_mix_072(self):
        self.assertEqual(mix(',knrg9csvmMxzzl3jxou@fehh7fxvp',
                             '&qqrd=ridmVimpz1ipyl1omvkObcvp'),
                         '1:xxx/2:iii/2:mmm/2:ppp/1:ff/1:hh/1:zz/2:dd/2:qq/2'
                         ':rr/=:vv')
    
    def test_mix_073(self):
        self.assertEqual(mix('Jiaeb%agvgEinksScplh;mcbaXfrkp',
                             'Tkmoe0kfio0eukf#ggyvStfeyBjzkj'),
                         '2:kkkk/1:aaa/2:eee/2:fff/1:bb/1:cc/1:ii/1:pp/2:jj/2'
                         ':oo/2:yy/=:gg')
    
    def test_mix_074(self):
        self.assertEqual(mix('+uzemQbbcsYrlgwKpolg7pabl@bctx',
                             'KmlckYmjldQeihnXmmikPbtfoPdabl'),
                         '1:bbbb/2:mmmm/=:lll/1:cc/1:gg/1:pp/2:dd/2:ii/2:kk')
    
    def test_mix_075(self):
        self.assertEqual(mix('ZhxjjWitca>hmmn0rrxv(rojt@wmne',
                             "'kvikBlmlvAyktjPrgop;vdqbDzsgi"),
                         '1:jjj/1:mmm/1:rrr/2:kkk/2:vvv/1:hh/1:nn/1:tt/1:xx/2'
                         ':gg/2:ii/2:ll')
    
    def test_mix_076(self):
        self.assertEqual(mix('%tfsxOgpcg1zsfw8bsav;xumzSvqus',
                             '+xxma&iiww<jpyc.ervx5icab-mqbm'),
                         '1:ssss/2:iii/2:mmm/2:xxx/1:ff/1:gg/1:uu/1:vv/1:zz/2'
                         ':aa/2:bb/2:cc/2:ww')
    
    def test_mix_077(self):
        self.assertEqual(mix('Gpfro1ezjzCjxyj<rdjz*dfcmNtbjw',
                             'XrivwNsuhl3zqrk1jynmBhkkd.yezk'),
                         '1:jjjjj/2:kkkk/1:zzz/1:dd/1:ff/2:hh/2:yy/=:rr')
    
    def test_mix_078(self):
        self.assertEqual(mix('Lllub.vctlZzbyqYnlox6irujCynmt',
                             '*mpqm6houq/zktdNxzbaFudyh:nghy'),
                         '1:llll/2:hhh/1:bb/1:nn/1:tt/2:dd/2:mm/2:qq/2:zz'
                         '/=:uu/=:yy')
    
    def test_mix_079(self):
        self.assertEqual(mix('Cijqz8nlbbMeekyXktvtLpasp+gvca',
                             '5muoo=wsuj=ucej3sknmHjvzsUfuoh'),
                         '2:uuuu/2:jjj/2:ooo/2:sss/1:aa/1:bb/1:ee/1:kk/1:pp/1'
                         ':tt/1:vv/2:mm')
    
    def test_mix_080(self):
        self.assertEqual(mix('FcpvuGftln$nhcqZuzydVmhtk*dtfg',
                             'Fviij:hxmgVwuvdVkkvw8owje@nxfk'),
                         '1:ttt/2:kkk/2:vvv/2:www/1:cc/1:dd/1:ff/1:hh/1:nn/1'
                         ':uu/2:ii/2:jj/2:xx')
    
    def test_mix_081(self):
        self.assertEqual(mix('Kgmon%sveq(fips-smvrSmdbm0zwwu',
                             'Rcbuy%ccrwSrhfaIgvwd*afdhNrxhk'),
                         '1:mmmm/1:sss/2:ccc/2:hhh/2:rrr/1:vv/2:aa/2:dd/2:ff'
                         '/=:ww')
    
    def test_mix_082(self):
        self.assertEqual(mix('<hkenShtsuZqsvgFspfq.daqn5gnqp',
                             '&fbzc?mawf-ggtl;ctlhOrtqr=ewxj'),
                         '1:qqqq/1:nnn/1:sss/2:ttt/1:hh/1:pp/2:cc/2:ff/2:ll/2'
                         ':rr/2:ww/=:gg')
    
    def test_mix_083(self):
        self.assertEqual(mix('0bjroPaiwv2miwbJxbix3deex8wbfj',
                             'Ojskn8qhryLfptvJnnagLwirlNduwz'),
                         '1:bbbb/1:iii/1:www/1:xxx/2:nnn/1:ee/1:jj/2:rr')
    
    def test_mix_084(self):
        self.assertEqual(mix('Ghese9bsvvNxool?yxkq-vienRymhb',
                             'RhsjpUjyud&ohqdHuuftCptgt$vlco'),
                         '1:eee/1:vvv/2:ttt/2:uuu/1:bb/1:ss/1:xx/1:yy/2:dd/2'
                         ':jj/2:pp/=:hh/=:oo')
    
    def test_mix_085(self):
        self.assertEqual(mix('%qzccKztkk?omqy6wpmj(noehLjzae',
                             'Ccwbp<zoam)pfilBsubjTuguo5kgrd'),
                         '1:zzz/2:uuu/1:cc/1:ee/1:jj/1:kk/1:mm/1:qq/2:bb/2:gg'
                         '/2:pp/=:oo')
    
    def test_mix_086(self):
        self.assertEqual(mix('6vzdoGrmzxNcnql.ujslPtavnZfnax',
                             '*dbdqMqewkAfmwu5qbpl5opcvEbrmw'),
                         '1:nnn/2:bbb/2:qqq/2:www/1:aa/1:ll/1:vv/1:xx/1:zz/2'
                         ':dd/2:mm/2:pp')
    
    def test_mix_087(self):
        self.assertEqual(mix('JafujFjqjbZljwr>udpn:eduqLhuqi',
                             '1atmfIhfwsKqxxnTuqsxEmlneZhhsd'),
                         '1:jjjj/1:uuuu/1:qqq/2:hhh/2:sss/2:xxx/1:dd/2:ff/2'
                         ':mm/2:nn')
    
    def test_mix_088(self):
        self.assertEqual(mix('Jhbju4snacGtlfyNldgvNvjhkEhppa',
                             '-srdcFvjfdKolfc=zvsb3kwrh;xnbz'),
                         '1:hhh/1:aa/1:jj/1:ll/1:pp/2:bb/2:cc/2:dd/2:ff/2:rr'
                         '/2:ss/2:zz/=:vv')
    
    def test_mix_089(self):
        self.assertEqual(mix('Zwlwy1yaxv&dvkn+jkkzMmepxFlvrr',
                             'Jnvfm5fbcl+ovtu@vgizCdxgi=qwet'),
                         '1:kkk/=:vvv/1:ll/1:rr/1:ww/1:xx/1:yy/2:ff/2:gg/2:ii'
                         '/2:tt')
    
    def test_mix_090(self):
        self.assertEqual(mix('Uxvxs+bknpYefzt=kjnm,upza/iseb',
                             "Hyncf'ayiaCvqja0ylnt6kytqDqmqn"),
                         '2:qqqq/2:yyyy/2:aaa/2:nnn/1:bb/1:ee/1:kk/1:pp/1:ss'
                         '/1:xx/1:zz/2:tt')
    
    def test_mix_091(self):
        self.assertEqual(mix('EsqjcHvsqlJfzilJsqay6aszr#bxbq',
                             'PutxrFbgbiKgbjt<qhwaDdpkyDqyqi'),
                         '1:qqqq/1:ssss/2:bbb/1:aa/1:ll/1:zz/2:gg/2:ii/2:tt/2'
                         ':yy')
    
    def test_mix_092(self):
        self.assertEqual(mix('Cwmyh4yrdqRsanf@beyp5iotc)eojn',
                             ">xtemPluqr1skvi'bcqbReeke@hhyl"),
                         '2:eeee/1:yyy/1:nn/1:oo/2:bb/2:hh/2:kk/2:ll/2:qq')
    
    def test_mix_093(self):
        self.assertEqual(mix('Wfdke9gmak>uzww.zqab2vmuzAvfav',
                             "'ahak#hnlg#otvbLsfnp&llah6telf"),
                         '2:llll/1:vvv/1:zzz/2:hhh/=:aaa/1:kk/1:mm/1:uu/1:ww'
                         '/2:nn/2:tt/=:ff')
    
    def test_mix_094(self):
        self.assertEqual(mix('Zjqoa2hxoy(fbrh(mgaaNvwekPveed',
                             '/qbsx.afbsFuxyy3jxqg#bsecMtqml'),
                         '1:aaa/1:eee/2:bbb/2:qqq/2:sss/2:xxx/1:hh/1:oo/1:vv'
                         '/2:yy')
    
    def test_mix_095(self):
        self.assertEqual(mix('UgqjeAkbdaMwyavQlehu@igxu?qxie',
                             ',gtmq*swfcCohysTrjva6wyxyUzqhn'),
                         '1:eee/2:yyy/1:aa/1:gg/1:ii/1:uu/1:xx/2:hh/2:ss/2:ww'
                         '/=:qq')
    
    def test_mix_096(self):
        self.assertEqual(mix('-lmwb1jrek0vsig*szlnYzjkz+ljrs',
                             '-qqwg:pomc5fpli?spgkFxlsj1kwxg'),
                         '1:jjj/1:lll/1:sss/1:zzz/2:ggg/2:ppp/1:rr/2:qq/2:ww'
                         '/2:xx/=:kk')
    
    def test_mix_097(self):
        self.assertEqual(mix("9gamoYuoqoYmsns'ojkpKgjcg/bcrg",
                             'DzforEhsod/llce.mskiYovrj7pzjj'),
                         '1:gggg/1:oooo/2:jjj/1:cc/1:mm/2:ll/2:rr/2:zz/=:ss')
    
    def test_mix_098(self):
        self.assertEqual(mix('Joijg+tnvgJngaxJhymz*bjjw$gtzi',
                             'WdsngDeabc0jpbf?uvteMxxet(kphj'),
                         '1:gggg/1:jjj/2:eee/1:ii/1:nn/1:zz/2:bb/2:pp/2:xx'
                         '/=:tt')
    
    def test_mix_099(self):
        self.assertEqual(mix('+nvpe=qioqOtslu&lahqYcxbhBgdck',
                             ')xizs#pnxd+dbrjRhzmvUnkzx/dief'),
                         '1:qqq/2:ddd/2:xxx/2:zzz/1:cc/1:hh/1:ll/2:ii/2:nn')
    
    def test_mix_100(self):
        self.assertEqual(mix('0mjskQcqsrHeuzj9enlg(kgiy9vxan',
                             '=cnoaDozfjPstxs8yatrAahlx)dpgy'),
                         '2:aaa/1:ee/1:gg/1:jj/1:kk/1:nn/2:oo/2:tt/2:xx/2:yy'
                         '/=:ss')
    
    def test_mix_101(self):
        self.assertEqual(mix('=zjshIwwtv&rvvv+nwga/ypcd2hkpa',
                             'Tdshu%gpwt%arqw:czrpVhgpu3kfoj'),
                         '1:vvvv/1:www/2:ppp/1:aa/2:gg/2:rr/2:uu/=:hh')
    
    def test_mix_102(self):
        self.assertEqual(mix('#rqaz#jihz-uugn=uosx<vefh-gcvr',
                             '2ehjzUsgdy>rora<dogvPjbzp<ixpd'),
                         '1:uuu/2:ddd/1:hh/1:vv/2:jj/2:oo/2:pp/=:gg/=:rr/=:zz')
    
    def test_mix_103(self):
        self.assertEqual(mix('.upst9mvem*txhiJrnsrNdigiHegge',
                             '?ybseCijvk(uhpl6voli@jjmbGvswt'),
                         '1:eee/1:ggg/1:iii/2:jjj/2:vvv/1:mm/1:rr/1:tt/2:bb/2'
                         ':ll/=:ss')
    
    def test_mix_104(self):
        self.assertEqual(mix('Smtuz$xzey:ihuxCmdpfHdclw<nokv',
                             'Dwzqu2kvgw4lxxv0byyv1ghhh:iebr'),
                         '2:hhh/2:vvv/1:dd/1:mm/1:uu/1:zz/2:bb/2:gg/2:ww/2:yy'
                         '/=:xx')
    
    def test_mix_105(self):
        self.assertEqual(mix('BohxlNmpwu:niizEnkjlDevdpJmwqq',
                             'IxcjjMacsv0kiph.jfnv&zywc+ozlr'),
                         '2:ccc/2:jjj/1:ii/1:ll/1:mm/1:nn/1:pp/1:qq/1:ww/2:vv'
                         '/2:zz')
