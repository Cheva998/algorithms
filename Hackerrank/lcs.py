# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:50:02 2020

@author: 320
"""
import re

def commonChild(s1, s2):
    #Test for empty strings
    if len(s1) == 0 or len(s2) == 0:
        return 0
    
    #Test for common strings, if not found return 0
    common = set(s1).intersection(set(s2)) 
    if len(common) == 0:
        return 0
    
    #Test for the same order of common strings, if true
    #return the lenght of the common strings
    patt = ''.join(common)
    patt = '[' + patt + ']'
    pos1 = re.findall(patt, s1)
    pos2 = re.findall(patt, s2)
    #pos1 = s1
    #pos2 = s2
    #print(patt, pos1, pos2, pos1 == pos2)
    if pos1 == pos2:
        return len(pos1)
    
    #Implementing the LCS matrix to find the lenght of 
    #common strings (only deletion)
    len1 = len(pos1)
    len2 = len(pos2)
    if  len1 < len2:
        xaxis = len1
        matrix = [0] * xaxis
        yaxis = len2
        x = ''.join(pos1)
        y = ''.join(pos2)
    else:
        xaxis = len2
        matrix = [0] * xaxis
        yaxis = len1
        x = ''.join(pos2)
        y = ''.join(pos1)

    for j in range(yaxis):
        for i in range(xaxis):
            if x[i] == y[j]:
                if i > 0:
                    matrix[i] = matrix[i-1] + 1
                else:
                    matrix[i] = matrix[i] + 1
            else:
                if i > 0:
                    matrix[i] = max(matrix[i-1], matrix[i])
                else:
                    matrix[i] = max(matrix[i],0)

    #    print(matrix)
    #print(xaxis, yaxis, x, y)
    return matrix[-1]

s1 = 'VGXGPUAMKXKSZHKBPPHYKINKEZPLVFJAQMOPODOTKRJZRIMLVUMUARENEXCFYCEBEURGVJYOSPDHVUYFVTVNRDYLUACVRAYGGWNPNZIJDIFYERVJAOALCGXOVLDQFZAORAHDIGYOJKNVIAZTPCMXLVOVAFHJPHVSHYFIQQTQBXJJMQNGQJHWKCEXECMDKMZAKBZRKJWQDYUXDVOOSSJOATRYXMBWXBWEXNAGMAYGZYFNZPQFTOBTAOTUAYXMWVZLLKUJIDHUKZWZCLTGQNGGUFTUAHALWVJWQNCKSIZGZAJKHYJUJLKSESZAFZJMDTSBYLDHYLCGKYNGVMHNEQYJDUGOFKLITXAOYKFOQKZSZNJYARKUPRERIVHUBPEHXMOYDAKKLBDNFHFXAMOTUBELZVBOZJARAEFMLOTFTNQRJOLVUAMAHNDEKFDSQCFVMQBOCBOMJXRQSFSKEVFXPHCQOQKBBOMCYURWLRNHRHCTNTZLYLVWULBDKCDPPGYKICHJTPUKFNLXFCEVKJEZQSMEYCANJLBESSRFAZDPRCOMDPJIMSFBUSLKSYVEERGCGMONCTCSVYPOLPLCGSQYFKILRIXODIWQCYREIWKRPIUIASFKJEXPFTZNQIBLSRJUYFSKNDAPWJEFUCDQCIUEHVFNDGHRXXNMVZLJXIOYUNDVPNDABSBNWOEYOMRJDCQCRXVYAHERMUDCCMUEAHEBYVSAKXWSEQZDUYFEZUJAFFDRSQFSEQSDFCGDENMRFWFNDIJTEPXHNVEDFBAGZRXKPRTGBOUKFXIWHFZFKSNAWGCUBSPXSIUYTQRWMVXFSVZLOTLFWIMLIYGNFDDESWMXUVHNQVJZGKPDZFJMCJCMSAASKEXTLSJRGGTYCGCQFPOQOMROUHJKNTQRYHJIFCXBYWHFUTFZMJCDLIVNUXMRDFGHKQLQZAEEAZKOOMVPYSJWNCYQYABUTSITEZURQHBUWABEXRCUIWAFNFVCASMRMBQNUPRUSKHSMEICAQQESYYVOPEPMVDOSIBRVQOGHDEIKBPQBFGRUFXDSQCHJKUXPXNGEBXRMQDGQJSOSENCRBWKNLLVUCVUBYOZFMTTXTLSRRNRQAVSHASZRENHLBZPNPJGQFTVWGUKJWSEKFCGLLBZLNVMOSMVQUBTWSGLTVMMZMSLQDXQIIFZKAQHSXZGUSEUEXLYCGUBHDNWHRSSYIYBITCOOWLHMMRDPGTRDWALVFFKNWIBHWHACQFJCMWUPOXONAVVXWSVPRPYMSKZNABSQUWSSUCXRMYWERFPZIQDZIYCNYNTHGMDAVYBZBQGCRGVWALCPTUTZXSQLKCHITHCDEZSAEFLDDFLGTIXBNAGKQRZESCKRIHWQPLFPSPKQVIFBMNQWIDBKZQIYGWFUNEFIWPXUEUMDWUGBFGNOJJRJPAFGKIRRUEOEZABCQLZMCDWMKLVYZVUUGHETWKXZUZFVOIRAREYBLWPRDNETKYIGXYQPZXECKYGYXTHSZXGYIDGLDNLZEQNDBVACJQYHFKQVLIUSQMXYEQYQORZMMJWSUICNYXQNKTYLAQNVBJLLTEXGRHIFDNEUGYSZNCRWGIDCFJGDZKOQFQBWEUCHTDVPIUNKPEHCSHTMRENTGSNDNBTBBBMOGUOPYPWKAPKRWISAMNXAGZFQSFSXTYXEPBPUMTLUJGXUENMZGGJMGIUTQOELTNLYBOQJEGCVUUIILMSBNALVBSFUTYARENKEWZLPWGQZFNNKEXXDSUFCJVRBKESROBOSUZUMUCCGMRSMXZTPSIQCHFCLVZKMVFMUSCNBRLCZVFZWMMKTUSAJDHOCMPRJLNDYDXROJJAHOCITARXLQXQJXQHPFZEWPYYKZEQJPEHSGIQVYEZBQWNPYUCIOBBLOXJXUOZSUVQWPHLHGLUFBHJGBPKXJXIYEUWMDUSFMLXKVQSMWYTKJOAKBNPGPHEFWPQNRBXWDAIPPUEOLNGEDDTRXPAXXZIWPHXKEINQSDIVGPLBCSZJHSXEICKSXBSEJHGMKIHTJCQQWXFTJSWWPTMGZPTQNOIXWPARKLAYJDSBIJTRGTXGZFCPUCHDSMKVQRHGDIIDNNUNWSXSCQQNNQMPCPKAGZSXMCBORWJYQNNOUSXHSDMKLMNDNTFUKMSKHNFJNFRVHQOMOFZKQIPTSIHALUJJXKBURWSBDLLAPWRQCARXMLZQWFCALVWXJFLFJTSTVRCTLBKBSJPNXYHSCXDXEPBWQECEWRZCITMDFBWZHIOWCPGGBUNWIOPNJDJCWRMIXZQULDIALDWRDJMBHVKGQYSPROVNZFRBAJESSMYBYCKDQMSXSRYDSKOIKTYFXJOMBTWYSKCTDJFQUVEKMCKRWIVZAYCTXCFXPTGRUPRMPNZSWUOEGWGDBBYPIRUISJQIBACPBOMBSJOQOZZSDGDRGYQYRFRKSSNTFGUDFQRQZXECGUCLNXEATMLQXSJKYJXIFIRSWZUDOLGMNLJJZJUJUAYJIICCERVHAVVGTCWHLSRWAQOTOGOKHTWGJMFQSLVHZPGNSFQHGBOEHMZPONRTKQJUANPNUFNLUEZLJSQVTOFMENWFZLGRRPZETXOGOBQRHUHLYGENSBKPWQBWWCZNXEIYOZTKMGCVJUSURKTIEHAHZRNTRRASIKBABWCSRHACZNXYUDGFPQDPGUIJAWGHWVVFOGDVTUHMORJCEOFCTZQYGFIETZKBEGKBSJZMFZRMFPMGVOAFXFYINMAYUXCJREDRYDNVLXWVHUEAIQGLUUFBBDTPVTCFHPRLYRBVVLNTRQZMQAWBSSRANJHAXTJVSXSDUOZSXLOEBLCIFBYFEUONSYRICVCCFPKZTIOALHQHQEKYDZQXMNZCAPLZLYXVFBPDZMLSFMMLGTNFRAROEBTFDUZXGPSAQWCNJIYTSRZYFWKRDLABYWHCMFGZVCYBFLKACYHHCKASMBLHBDJEOJNFWYLCQVNBMZXUGFSIYJGUICGFFIWRSZZDBZJYHVGPNFSAPUFJQFESPXBFLJGTDGSMFEECQFWFVKWEIACDITMSNFALDCQLRYCLLMCCMODLNLBKWVGMDZWAPSBZYRWXASQVCTBMTBPIDEDMVRPXQNDCAHLTGZSHJARUUEMQUXRRVTHOHCDKUURWURKWEXHYPSBUPXUISDESHLTSVFHVJVHNXGGARVCDAIIAQADYJJERNIDPERSJDQUCSAUPRZTYFOIIKLHTJSZNDDFTCGELCHWBIZHESDUXMACMZILDECEGSHHNTFZNBBBGXAVMPNFLHPXYLXKYZTWBQWPUYMQLNXMETGHTNREFEYPIVPYNDOBBRESGVLMKKXWHLOMIGIRIZLNGKYKRYMHEYWUJWMJHNZXMGMKQGSAJKYKVQJYAPLNWKCUBVBXDXYHECCRZFNEHQEIZVICXXXESNSSFEUZHSJDHXNDDSIUVXANFKPEQODIRLSYWLYMIWSHVENLIUOMFLSYIQACJUAJHXMEKLFADFVXVMPKNEDSHBYVENBOQUEAAIQWEXNQGQVJWZFOFOKVKGDGZHWRTKTDBERAPDNUMYTFOBBQCOZOJIVHKNGVYYSTJGSDFNOSJLRXPZFENFYHWAJCJUPUWYUVKORVMIUPLWVOOOJCKJMAQYSPYACDNGDNMUYRSOISLCMORSFGZZKSPOSLTNXPVOHDSPMZKEWHWNJMMMGIQUYWBYJIOWEWRVFLTAJJRDUGEJYJRKWAZOGERWKHVGTQUXUXHRUBFRQYFARBIAEPORGWQUIJHBUWQVEJGCOJNCYUOPFGFPTTEUSXAJVQYNZZISGNXJHJETOMWBTTPGBSZZUWRFNORZXTOMUWNQPKUTTCBYBDHLUVCEXTUOXMZGIBULSZOBTMXUTCCLNYXCDFHZNMWHESGEZPVXPYCZLCGYAQNKGIJUKIIIUCJFUEQBMXQNWDCYBERSZMOFRWOCLBYNJWJCRQAYJPCIJNDYZMCTZBAOQEUGWRMHPKZVYYGKOVPCKBZETSHNEBUHTMQQPMBWSEOCXEOBHDJMKFMZVMKEZWOMLYZPAGRXGXYBZTSXAEUNETDTIKJBBXUQJCDWYHWREGFYJHCTUARLQOFGWHPYUTWRBYEBFSSWBRCZWXKLTZJGMFUXARYDAGGOJPHEUSIUBPMQJMHOCQMVJOSPDFLIVMSRCQTWGXDAZUNYTIFHXQUASVCGDLOZUQZWHFSSRCXARCJFLFTMWNGZONWFSVTUKXVBSOUBBBPBFWJFNGELEKPMOADIZDSORTKABMSWCMYWNBAJXNKVMNDBVTCPNJXWMODDNTSQTHUSVZMKUEDBDKBIQDWPWPSSRJJFLSWUFMHCLMNSTZUBTCVQVQSDSSGSCJYQZWCAMNVRILESSQPZGQXDLSNCLUJDSAQBXXYLTZLQWLUORTKQADJCQUQDQCSVIXGWGLWRRMKHDSBEBBJVCGZLWTBVASPHVMNFVFJYKQMIMWXEMMAHHMZOADAPWORUVLPQOLWBMKESKAFYZBVZVMMPRWAXISDUKVMBVCVZWXYNRTKSBDZKVAGIHFGIQMSDEJXIRROWIRGQVZELYSOHWVJFALSGXGZOKBFURVECUXSIPQVRWQJOSFYBNCIHPZJCBXEFZVRIISGFIPSIAPDPBSSGLQJUHVQRXEFPTIMXEDAHMJQTVIQRXNFPOYSAKXHXRJETYDSXIXVXYUJBVQAVXZUPQPZDQLNDDXFANWNKTLPJCCPWUYGXYYXUAFYPZOAKDXPKAHVPJJFDOGNZBYIXYBMKDAQLIXEUTOJGTDJLTWPXPVUMBUDCKMDXRHQWKRRLLTGXDYOAOKDPARWBANIDRFSSIUIGZDUWZEJBBNUOIWQLSGTESHSCNVLMJYIWHAGTIMRQTFFKFGBODLWXIRGRMRDHLIHYAMXMOLBYFWCDPUTEDZCWSKRPKYKQYPKSLSQNFNDIGWHJPDQMACLGNEBLKQCEPSNLJBYOYXCHDIYYGWCHTCOXYZZBLNCVOSGCFFRHAS'
s2 = 'EVYRFZJIZJBKRFPPCJBHDPBYICJMVXNSXRLFUPSNIYCHUTSVGWTRJVNEPWFSSFOVSAXKHENZIDOHUQRMXXUMFDDYGFEYPTZCOURHVEDKDOACAMYUOYEINZLVOCYDNXYKXPFKXWMDOCFZGCBWJJZRJZVSLTCPVUHZNZLVNZBDQYJXQWGBTLLQADGXJFZRTMMVBDKCZRKYLNZEJAIPLDLCTXVKLOFQNQFFKYDZGTFBFERGKEQMCVYLZQIIUOCWGDVICASICRUGGKBSRGYLDPIWKURUYIHBERGCGGXWUJDPROKXYKQQBUITESPOHBQNKQKUGWHLHKGABAPHQTFDBFHGVBLUYXWZOPSQEUKCLFKFWKXQWZAKBWBHILYFKYOIITLSHCNCYQDMJNFJEKJJDZQSWMJVNDTMYANVUCNZBDUAMHAPYNGGABONFABHVNQMKSNYHYYDLHKFHHDKHVSUSNWPPWDWVAYFKSMBSXUJUVLAIGWMQSNZYTVWBPLYYDSPRLUCGXOAAJLLVQIIHBCKZLPASFSNSUSYFHBMCBFOSTWISFNREQQYTKDCAHMKZTUAXOJIFTFVWWVMODLJMNBJEOIFEYNMAXZKTXXPEDAGSNZUVFRKIGJDCKUZOSKNADBFLGISKPPHYGXZMCMFAZJXAZHBQBQRREZXLNIOKHFKKPDRHTCRUEQXLXXDCVJLXISJXAWESPGXOXJYGEOQZEMXIKVPQRFQBXYARJWOJEKEXBQAEDYUIPLLDVKYKWPWMZHEIQGDNKSFYMIUINMORLIZMXMLHXSJOTKROYPHYKJHRBEXHAFVCJETIIMMPQKSPSPLOAYAPWBXUJWJBBIHVGVKDCFPABBAYMCZPIMZTOQBIDTJSDNKGUDECSFSRREZFBTUXIXJKIPXTNCFQUQDTANIWLEVDYODLIIWUVBOGQZWWPURCQVRYSJZDBSUCBXNLKFGCVWAGOIQIGSNVKWEMYBVXUAERMVJJLDZSPJKPVEOFJVPVGVOKSJYIFNLGBRUBYVNDYNHVLUDRYLJRGBKYSZBXNVDBYAHLZTQXUIBBOTBFKHSGYKPGCRWLMXZMHIOVKLIJTBUTFDIOJSCLMCJTTAFLMSYDWUNHEIKKSKJHXADKTUYNCEYAJDKVEIMKSQWLOGDYYDDKSRARLPGFZZNZUAJFRFEUNQJUAWJHFMARNJUIYEUZTDVRZHCEZVSFKHCDGTTNPFNKHSYPMXBOBNQYLLOAKFKNOYPEORITDIQRKMJIFOUEIBYCUXNQNUNBTNLNKCIOHEFUQCYFOBIIYBUWPRQRFOKONIRFILFQGJHFPLYASYJMZQPDWTSBKGQCYUVTBUNQNHNAEFGPJNVAGTPXFQRGMXTSVAJTRPBDBNZQACKJDTAMMEUASETGWFZWBYSFOMABHMXHLNQTBALMJFHXROGODUKWEYZMJFHKIIATYPLTUNTSXAJRCDZFJWFXRQWHPOSVXEDXOMRDMBQHAVOCMVTKGGPULOVCCKLEYCFGTYPCNCNHTWUWRMZJPBSCIMPXCZRPBIXQVAMEGSEYPGECDDFOFLQTASXNGKYWTAIRATEGYVZXTTVBFDDKWXOBEZXFNWPZXKJCDPNLVWOZNDNFEGUHYCDOOMTXBPIQLQWOTOIBBQZWXVGKMQWOWATZOZGBTRDKNDCPIVAILDYXKKNZYIYYTBFLWPAITVIRSPTZDHLFSIABOMDXQHTFNVLEUOUKTABUAWPRTURPUMHGKBUACFFFOXRIUGZAQSENYFNMGQJMSJVOBAEUQKGWPYVWPAFBNXIODTCEMCDQAXVLNYCQYVAXXYBHVDKHIUHPVUMQBFRYWTQKUVJJEAEXYCJZHRFCLDUGQRVIYLXUBXWGTCPTVELFADQXBCVTSEZNBBUAEUDGEJCVYTASTWCZYJQHGLYHZTGDDICBNLVYTJHMHENXSDHVLYFLHZQSOIDECOJQGXSQKHVFKPLDTOQYRGADZGIOOLYNWZXJRUIIYBWCNWAUPWGMUEQDFYVSVLBHQQXKCEEBMWQJYPIYGYZCDBZPKYRHROJQMQSBJILAMAKICREORUIJZRHWWFKBVZUAJRSCCDHBKUNZVWRHSIPHMBDAMNNQKHTFKYQRDRCEXZFTUAXFRPHOIPMZXCZJCUOQCZGPRMZIOTDISOSKROXJKLEAHTIRTMVEUCAYQVJBJCRNDJVXVVOUMPCGCZWUMAAPDEPSHNAIMATOLVNLMEPBJZWXMACWILFYKKKUYSUCCMFTJUOCCUPAGBYAKRUGNNSGRVBXDWGTQZZWHBKYJDKFNIEPBOLVIWSBEVYPMEKZMEVXOHKSLYLOSUSKCVEHBYRRUYKOHNENCVYODSTLPWDWOOONHNIYEGMYEKMTOPUWYKWCTHHDWZQXOCNQGZMTCTBPUILLKMAWSSJTRGXLSPQQYCZVKHHFCUGLIDEMBZUNQFSPCPHJQTUAYWQBJJSQYDFOJZOFIRJWOIOBXHFDIMSVISXEYYRKSQALVHUQLQOJZVDMADAIUKMJQGFAFJQOYWDFXPMBUOXOEISIHWBLFTQBSBCMQSKWMHNWOJRJOOAHBBKCVKSOGUCZQZVRPBMDKQYICBHJAZSCXKVRMBXHUGUZXFEJGUIANOFATRARRNZPYVBLJZTDZLRFIZBLVXKJRFACEVLDDQMRGZYUHJFBVPVLZJFNBKPKUFNAOEJEQNSNKITMIGJVIBPVIJTBEVSSVLCQZMSHQNDHZHXGGCTDZPOGABKKJTNIXVVGXHKRYILLFJMJHNKKDIQWGPPVJVCBWEQOVKIDJEBMKOLZGSLHMRHIQGLVWHICMTOXPITUPETITSOBUIWYRKMZMWFMSGFOORVZEBZPVBSCVETJKNHNQTJHNINAVAWQHPKHBCSAGDNLYAADUSPPTMGECGCBYDSMNGFPLHLMEQPDUYJVIRVRZFBRFMQKEWXOTZGTHMVBXBNUYACTBIRPPWWYMERCDUZTLKJJMXGBHFINZEEZPOFNCRTDYCEPYBZWNHKZXKNJNOTDVKFKXWKWOBTKAWEBEZAJMLPFUXOAQMEEAPDEWVJDVHMJIFZVPJKAZWPCVLRUWWXATRFIEKSQFVFIGJWYTMBMLLCQPQJNELFQLBCGLODVHXBWJNTQPKEMPRBWNAVCPJWKCIEKOOVBCMSLERUKVJCQAIXQBCHUXCDIQCSOTCHLQBYAXHWAJAFWZAQMHRTXMFDIWFFYQTVVSWXGIDAOHUHDQSYMOZESUHIEHBBCHTPTSBKBWVRSVNDQYSXMWNDBAECMHPOPMSAUCXOHITLWDNCPBVMKCUDAJESJBGMVXVTPBOOPAEGUGLKUJIIZPQPQVYPIBOOOBDOJUFCVEWMZMADYLIHDJJYALDZXDYNFCKNHQBIJHMAJWMYIYKCNGPRIVZMOUZRXRFVMZSDHAQJEOGJYEJIWHZSEHQVUBFNEFKFLTAFNFCDXNMJIXQNOPGMYVZUVWUFVKFXMYCBBQIUBWEVLYJHDSMZEDRJWVLPVCXJLPNACMEHOWHRJIEEXEAVAHUQYRYHEGRGDBHSGQAHFIIHVPSVXGQJRGOBNTLFILNFPMIDKEHUQBJHCKHBCWEWFAIILHINFVDOJBDLPGNPRTORKRMMCZNCYWFYDRTUYOTFRMZVPHRKKTERJKIJUWCVJANXEQWCUIXLWFUEGNPHHKELAKDLTQEEBMUUQHEJPOBTDLYRFBZGUOKCWARIBQJCUUBQLYRUMVCRGTEIYUDJIDIPZNNGMPNFIONDGFQGPEQPGEKNHEJMNTASLYRZUYKRIIERZLIDIHPEBYIBUDVYNXGVVKLOQPDVRNYLINDKNAEHTDIOLSUFZGOXGOFOFURIVLOCFBPGCYOCVBGFMKALQZNBKWNZPKIQWRLIMNKBBXJPQHCTUXAHUQTFBRBKDAFALDVVZRRPLOEVUCBUDBUUUFWFGBUWGKAKDRYCBVLOSSJZHSCYIXWOYBDUWSBFKSHSKVZLBNDNHNCZSKZNQIUUUYNVRDUPFJORXZDEVVRNGHYBKQEANYEYJDCQXPHEKNPAKRGZTODMNJKQZAICVLWCIWYDFSRDDBGVFKCOCZAZKDUBFTKLNYPTMRKJIOKPECEIBEABQGCKLJYMBIACXYPKNGHOKWBIPGLAXBVXKWCJCDGHCKWAZBRDFRNTZBZVCTXKTQNXTNGQWVAPWVLZXPXCSIOJWHWTZYXLZUSVTRYNJXQZBBVZXFBHJCDAWJAUJUUGLNTLCNIGZINJUAZHHOZCTXPCRNSMQBEEZWHIBSEAFALDETCFKCVLMQCCLZIVVZUMHGAEPAIFGSCINZQJEDNTSYGVTWSQWREKGFEUSLRZYXXTXABLAWYWMPYFXBIGRRITWTELCILVQRNWLJMNBSCILFZOUJGRGQWZDGXZWSVKVWQTMUKXZDCYDENZNEIMHXWYATJEMDEQTXYPMVFEKHSPZFXHYKPGWLSJCDOBYFGEUGOVJNXOTXKDHJTIFFTJWHHDXCNWOLPHGOHJORXKQUCTLSDMGSVRDUPWVZRUSEDIOMVFSYERIWIXVPSMHIISMNSWPVAQEIXIRJNABCAPOHKXTFXZANQJUSTEAOCTNXACBOTRLXHGLSXMHMATZXFLTFJDAIYSQSZEJUPSBRGFEGHBWIJAVFINBBCFQRPUTGARLCNJYHZIADZPSUBZPEYPEFLUGWPGIFNXTGBJCGRLVVBMDKLGNYPLZBXZQSSQYLZZTKJLNMXMSLBOCOXQPGDARJAFTDZCVJSPXXIZQIEHGYOBWULEYAZGISEMUWVNCIPBDJCLIWBCPKZKPUQFTITGLWJTLHALWOUYGHRGJWRCNNRSAELAKVVUXUGYMUKRJBYFKYENHZBDTQEBVLTGLCJSEJWJUZCYNCMRIUQNNCNIAGCTKLFEZDFWKHLPIWZCZGHYCJLJQWVKMDNBJNKIZWBWHQWPPJNREFYQMCDUGXMDDRUAYHZUNFGCKDDZSJAKIEYZCZRHEFNJXLISNBITZYWZEDQNQCPAXPTG'

print(commonChild(s1, s2))