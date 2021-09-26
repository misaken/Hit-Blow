import random

while True:
    options=input('Hit&Blow　    始めますか？　y/n　>>> ')
    if options == 'y':
        
        while True:
            print('o:設定を開く')
            print('s:ゲームをスタートする')
            print('f:ゲームを終了する')
            start=input('>>>')
            if start == 's':

                f=open('Hit&Blow_digit.txt','r')
                for row in f:
                    digit=(row.strip())
                f.close
                h_count=0

                print('スタート！！\n')
                print('*/*/*/*/*/数字当てゲーム/*/*/*/*/*\n')
                print('--<ルール説明>--------------------------------------------')
                print('|  入力した数字のうち、値も順番もあっている数の個数をH   |')
                print('|  値はあっているが順番が間違えている数の個数をBとする　 |')
                print('|  ただし０を含まない'+str(digit)+'桁の数列で行う                     |')
                print('|  なお中断したい場合は"break"を入力してください         |')
                print('----------------------------------------------------------')
                
                b_list=random.sample(range(1,9),int(digit))
                #print(b_list)

                count=10

                while True:

                    ass=input('入力して下さい(残り'+str(count)+'回)...')
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
                                B+=1
                            elif i in b_list:
                                B+=1
                            else:
                                pass
                        count-=1
                        if H==int(digit):
                            print('クリアです')
                            now_records=10-count
                            f=open('Hit&Blow_records.txt','r')
                            for row in f:
                                old_records=(row.strip())
                            f.close()

                                
                            if now_records < (int(old_records)):
                                f=open('Hit&Blow_records.txt','w')
                                f.write(str(now_records))
                                f.close()
                                print('***祝***')
                                print('NEW RECORD:'+str(now_records))
                                print('新記録として保存されます')

                            else:
                                print('現在の最高記録:'+str(old_records))
                                print('次こそは更新しよう！')

                            break

                        if count==0:
                            print('ゲームオーバー')
                            print('正解:'+str(b_list))
                            break

                        print('ヒントです　　H:'+str(H)+'   B:'+str(B))
                        print('------------------------------------------')
            elif start == 'o':
                print('<Options>')
                while True:
                    f=open('Hit&Blow_digit.txt','r')
                    for row in f:
                        digit=(row.strip())
                    f.close
                    f=open('Hit&Blow_records.txt','r')
                    for row in f:
                        old_records=(row.strip())
                    f.close
                    #print('r:これまでの記録を変更します['+str(old_records)+']')
                    print('d:桁数を変更します['+str(digit)+']')
                    print('f:<Options>を終了します')
                    m=input('>>>')
                    if m == 'd':
                        while True:
                            d=input('何桁に変更しますか？>>>')
                            if not d.isdigit():
                                print('数字以外が入力されています')
                            elif int(d) >= 9 :
                                print('正しく入力されていません')
                            else:
                                f=open('Hit&Blow_digit.txt','w')
                                f.write(str(d))
                                f.close
                                break
                    elif m == 'f':
                        print('終了します')
                        break
                    else:
                        pass
            elif start == 'f':
                print('Hit&Blowを終了します')
                break
            else:
                print('正しく入力されていません')

    elif options == 'n':
        break
    else:
        print('正しく入力されていません')
