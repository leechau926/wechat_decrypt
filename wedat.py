import os

def imageDecode(dat_dir,dat_file_name):
    dat_read = open(dat_dir, "rb")
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    out=target_path+"\\"+dat_file_name+".jpg"
    png_write = open(out, "wb")
    for now in dat_read:
        for nowByte in now:
            newByte = nowByte ^ xor_value
            png_write.write(bytes([newByte]))
    dat_read.close()
    png_write.close()

def findFile(dat_path):
    fsinfo = os.listdir(dat_path)
    for dat_file_name in fsinfo:
        temp_path = os.path.join(dat_path, dat_file_name)
        if not os.path.isdir(temp_path):
            print('文件路径: {}' .format(temp_path))
            imageDecode(temp_path,dat_file_name)
        else:
            pass
                        
if __name__=='__main__':

	# 修改dat文件的存放路径
    dat_path = r'F:\2020-06'
    
    # 修改转换成jpg图片后的存放路径
    target_path = r'G:\newfolder'
    
    # 修改加密的异或值
    # 异或值后两位=FF^加密文件第一个字节
    # 用FF是因为jpg文件开头就是FF
    xor_value = 0x24
    
    findFile(dat_path)
