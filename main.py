import random, json

print('*/*/*/*/*/数字当てゲーム/*/*/*/*/*\n'\
      '--<ルール説明>---------------------------------------------------------\n'\
      '|  0 ~ 9からなる任意の桁数の値を当てよう！                            |\n'\
      '|  入力した数のうち、値も順番も完全に一致してるものの個数を「Hit」、  |\n'\
      '|  値はあっているが順番が間違えているものの個数を「Blow」とする。     |\n'\
      '|                                                                     |\n'\
      '|  制限回数以内に値を当てることができればゲームクリア！！             |\n'\
      '|  最速記録の場合はレコードに記録されます。                           |\n'\
      '-----------------------------------------------------------------------')
while True:
    options=input('Hit&Blow　    始めますか？　y/n　>>> ')
    if options == 'y':
        digit = int(input("当てる値の桁数を決めてください。\n>>>"))
        with open("record.json") as f:
            jsn = json.load(f)
        counter = jsn["{}".format(digit)]["count"]
        count = counter
        old_record = jsn["{}".format(digit)]["record"]
        h_count=0
        b_list=random.sample(range(1,9),int(digit))
        print(b_list)
        print("-------------------------------\n"\
              "桁数 : {}\n"\
              "制限回数 : {}\n"\
              "現在の最速記録 : {}　　です。\n"\
              "ゲームスタート！！\n"\
              "( 途中で中止したい場合は'break'と入力してください )\n"\
              "-------------------------------".format(digit, count, old_record))
        while True:
            ass=input('入力して下さい(残り'+str(counter)+'回)...')
            if ass=='break':
                print('終了します')
                break
            elif ass=='hint':
                if h_count==0:
                    h=random.randint(1,4)
                    print('ヒント:'+str(h)+'桁目の数字は'+str(b_list[int(h)-1])+'です')
                    h_count+=1
                else:
                    print('ヒントは一回すでに使用しているので利用できません')
            elif not ass.isdigit():
                print('数字以外が入力されています')
            elif len(ass)!=int(digit):
                print('入力されたのが'+str(digit)+'桁ではありません')
            else:
                ass_list=list(map(int,ass))
                print(ass_list)

                H=0
                B=0
                for i,j in zip(ass_list,b_list):
                    if i==j:
                        H+=1
                        #B+=1
                    elif i in b_list:
                        B+=1
                    else:
                        pass
                counter-=1
                if H==int(digit):
                    print('クリアです')
                    new_record=count-counter                        
                    if new_record < (int(old_record)):
                        jsn["{}".format(digit)]["record"] = new_record
                        with open("record.json", "w") as f:
                            json.dump(jsn, f, indent=4)
                        print('***祝***')
                        print('NEW RECORD:'+str(new_record))
                        print('新記録として保存されました！！')

                    else:
                        print('記録更新ならず...次こそは更新しよう！')

                    break

                if counter==0:
                    print('ゲームオーバー')
                    print('正解 : {}\n\n'.format(b_list))
                    break

                print('Hit:'+str(H)+'   Blow:'+str(B))
                print('------------------------------------------')
    elif options == 'n':
        break
    else:
        print('正しく入力されていません')
