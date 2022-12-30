from Cryptodome.Cipher import AES
import operator                     # 导入 operator，用于比较原始数据与加解密后的数据
import time

AES_BLOCK_SIZE = AES.block_size     # AES 加密数据块大小, 只能是16
AES_KEY_SIZE = 16                   # AES 密钥长度（单位字节），可选 16、24、32，对应 128、192、256 位密钥
key = "ok let's go"                 # AES 加解密密钥


# 待加密文本补齐到 block size 的整数倍
def PadTest(bytes):
    while len(bytes) % AES_BLOCK_SIZE != 0:     # 循环直到补齐 AES_BLOCK_SIZE 的倍数
        bytes += ' '.encode()                   # 通过补空格（不影响源文件的可读）来补齐
    return bytes                                # 返回补齐后的字节列表

# 待加密的密钥补齐到对应的位数
def PadKey(key):
    if len(key) > AES_KEY_SIZE:                 # 如果密钥长度超过 AES_KEY_SIZE
        return key[:AES_KEY_SIZE]               # 截取前面部分作为密钥并返回
    while len(key) % AES_KEY_SIZE != 0:         # 不到 AES_KEY_SIZE 长度则补齐
        key += ' '.encode()                     # 补齐的字符可用任意字符代替
    return key                                  # 返回补齐后的密钥

# AES 加密
def EnCrypt(key, bytes):
    myCipher = AES.new(key, AES.MODE_ECB)       # 新建一个 AES 算法实例，使用 ECB（电子密码本）模式
    encryptData = myCipher.encrypt(bytes)       # 调用加密方法，得到加密后的数据
    return encryptData                          # 返回加密数据

# AES 解密
def DeCrypt(key, encryptData):
    myCipher = AES.new(key, AES.MODE_ECB)       # 新建一个 AES 算法实例，使用 ECB（电子密码本）模式
    bytes = myCipher.decrypt(encryptData)       # 调用解密方法，得到解密后的数据
    return bytes                                # 返回解密数据

def start(key):
    # with open('C:/Users/MI/Desktop/data.txt', 'rb') as f:          # 以二进制模式打开文件
    with open('C:/Users/MI/Desktop/Ebook/深入理解计算机系统.pdf', 'rb') as f:          # 以二进制模式打开文件
        bytes = f.read()                                # 将文件内容读取出来到字节列表中
        print('源文件长度：{}'.format(len(bytes)))
    key = PadKey(key.encode())                          # 将密钥转换位字节列表并补齐密钥
    bytes = PadTest(bytes)                              # 补齐原始数据
    print('补齐后的源文件长度：{}'.format(len(bytes)))

    print("----------",cnt," 开始加密----------")
    time_begin = time.time()
    encryptTest = EnCrypt(key, bytes)                   # 利用密钥对原始数据进行加密
    decryptTest = DeCrypt(key, encryptTest)             # 利用密钥对加密的数据进行解密
    time_end = time.time()
    t = time_end - time_begin
    print('time:', t)
    print('----------',cnt,' 加密结束----------')

    if operator.eq(bytes, decryptTest) == True:         # 检查加解密是否成功
        print('AES 加解密成功！')
    else:
        print('AES 加解密失败，解密数据与元数据不相等')
    return t

# 主函数，从这里开始执行
if __name__ == '__main__':
    cnt = 10
    T = 0
    while cnt:
        T+=start(key)
        cnt-=1
    avg = T/10
    print("总时间为：", T, "平均时间为：", avg)
