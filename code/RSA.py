import math
import random
import time

filepaths = []

#生成小于max_num的素数
def gen_prime_num(max_num):             
    prime_num=[]
    for i in range(2,max_num):
        temp=0
        sqrt_max_num=int(math.sqrt(i))+1
        for j in range(2,sqrt_max_num):
            if i%j==0:
                temp=j
                break
        if temp==0:
            prime_num.append(i)
    return prime_num
 
#生成公私钥
def gen_rsa_key():              
    prime=gen_prime_num(500)
    '''
    print(prime[-80:-1])
    while 1:
        prime_str=input("\n 请从上面选择两个数字，以逗号隔开: ").split(",")
        p,q=[int(x) for x in prime_str]
        if (p in prime) and (q in prime):
            break
        else:
            print("输入错误！")
    '''
    p=random.choice(prime[-50:-1])              #从后50个素数中随机选择一个作为p
    q=random.choice(prime[-50:-1])                  #从后50个素数中随机选择一个作为q
    while(p==q):                        #如果p和q相等则重新选择
        q=random.choice(prime[-50:-1])
    N=p*q
    r=(p-1)*(q-1)
    r_prime=gen_prime_num(r)
    r_len=len(r_prime)
    e=r_prime[int(random.uniform(0,r_len))]
    d=0
    for n in range(2,r):
        if (e*n)%r==1:
            d=n
            break
    return ((N,e),(N,d))
 
#使用公钥进行加密
def encrypt(pub_key,origal):            
    N,e=pub_key
    return (origal**e)%N
    
#使用私钥进行解密
def decrypt(pri_key,encry):             
    N,d=pri_key
    return (encry**d)%N

#将字符串写入文件
def write_file(str,str_filename):
    try:
        f = open(str_filename,'w',encoding='utf-8')
        f.write(str)
        f.close
        print(str_filename+'文件写入成功！')
    except IOError:
        print(str_filename+'文件写入错误！')

#读取文件内容
def read_file(str_filename):
    try:
        f = open(str_filename,'r',encoding = 'utf-8')
        s = f.read()
        f.close
        # print(str_filename+'文件读取成功！')
        #print('文件内容为：')
        #print(s)
        return s
    except IOError:
        print(str_filename+'文件读取错误！')

#选择模式
def start():
    pub_key,pri_key=gen_rsa_key()
    # print("公钥：",pub_key)
    # print("私钥：",pri_key)

    N = pub_key[0]
    e = pri_key[1]
    pub_key = (N,e)
    # filename = input('请输入你要加密的文件名：')
    filename = 'C:/Users/MI/Desktop/data.txt'
    origal_text = read_file(filename)                   #读取文件中的明文
    print("----------",cnt," 开始加密----------")
    time_begin = time.time()
    encrypt_text=[encrypt(pub_key,ord(x)) for x in origal_text]             #对明文进行加密
    # encrypt_show=",".join([str(x) for x in encrypt_text])               #将加密后的内容输出
    # write_file(encrypt_show,filename)               #将加密后的内容写回文件
    time_end = time.time()
    t = time_end - time_begin
    print('time:', t)
    print('----------',cnt,' 加密结束----------')
    return t
    # else: 
    #     print('输入错误！')
      
if __name__=='__main__':
    cnt = 10
    T = 0
    while cnt:
        T+=start()
        cnt-=1
    avg = T/10
    print("总时间为：", T, "平均时间为：", avg)