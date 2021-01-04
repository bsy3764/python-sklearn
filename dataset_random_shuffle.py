import os, random, shutil

src_path = '/home/user/Downloads/test/'    # 기존 아이템 폴더를 확인할 수 있는 경로
dst_path = '/home/user/Downloads/test/'    # 아이템 별 폴더를 생성할 경로
train_path = os.path.join(dst_path, "train")    # train 데이터가 이동할 경로
validation_path = os.path.join(dst_path, "validation")  # validation 데이터가 이동할 경로
product = ['img']
img_list = []   # 기존 디렉토리에 있는 이미지 파일(.jpg)파일만 모아둘 리스트
txt_list = []   # 기존 디렉토리에 있는 텍스트 파일(.txt)파일만 모아둘 리스트

train_img = []  # train 디렉토리로 이동할 이미지 파일을 모아둘 리스트
train_fname = []    # train 디렉토리로 이동할 이미지 파일와 같은 이름(split함)에 .txt 를 붙여서 모아둘 리스트
train_txt = []  # train 이미지와 같은 이름의 텍스트 파일을 모아둘 리스트
no_train_txt = []   # train 이미지와 같은 이름의 텍스트 파일이 없을 경우 모아둘 리스트

validation_img = [] # validation 디렉토리로 이동할 이미지 파일을 모아둘 리스트
validation_fname = []   # validation 디렉토리로 이동할 이미지 파일와 같은 이름(split함)에 .txt 를 붙여서 모아둘 리스트
validation_txt = [] # validation 이미지와 같은 이름의 텍스트 파일을 모아둘 리스트
no_validation_txt = []  # validation 이미지와 같은 이름의 텍스트 파일이 없을 경우 모아둘 리스트


for i in product:
    #본인 컴퓨터 경로 입력
    print("product : " + i)
    path = os.path.join(src_path, i)    # 기존 디렉토리 경로
    if os.path.isdir(path) == True:    # 디렉토리가 존재한다면
        print('{} 파일 위치 확인'.format(i))
        src_list = os.listdir(path)
        src_list_len = len(src_list)

        # 이미지 파일(.jpg)파일만 가져오기
        for j in range(src_list_len):
            if '.txt' not in src_list[j]:
                img_list.append(src_list[j])
                img_list_len = len(img_list)
        print(img_list_len, type(img_list_len))

        # 텍스트 파일(.txt)파일만 가져오기
        for k in range(src_list_len):
            if '.jpg' not in src_list[k]:
                txt_list.append(src_list[k])
                txt_list_len = len(txt_list)

        # train, validation의 비율 정하기(train, validation 데이터셋의 개수)
        train_set_len = int(img_list_len / 10) * 8
        validation_set_len = int(img_list_len / 10) * 2
        # test_set_len = int(img_list_len / 10) * 2
        print("image list :{}".format(img_list), type(img_list))
        print("trian : {}, validation : {}".format\
                  (train_set_len, validation_set_len))

        # train set의 저장 경로가 있는지 체크
        if os.path.isdir(train_path) == False:
            print("train dir 없음")
            os.mkdir(train_path)
            print("train dir 생성")
        else:
            print("train dir 있음")

        # validation set의 저장 경로가 있는지 체크
        if os.path.isdir(validation_path) == False:
            print("validation dir 없음")
            os.mkdir(validation_path)
            print("validation dir 생성")
        else:
            print("train dir 있음")

        # train과 validation의 이미지들을 랜덤으로 비율(데이터셋 개수)만큼 추출하기
        # 이미지를 바로 가져오지 않고 이미지의 index의 번호를 랜덤으로 가져오기
        train_num = random.sample(range(0, img_list_len - 1), train_set_len)
        validation_num = random.sample(range(0, img_list_len - 1), validation_set_len)
        print("train : {}".format(train_num))
        print("validation : {}".format(validation_num))

        # 위에서 랜덤으로 가져온 index를 가지고 해당 이미지들을 가져오기 : train_img
        # 이미지 파일을 파일명만(확장자 제거) 가져오기 : train_fname
        for l in range(img_list_len):
            if l in train_num:
                train_img.append(img_list[l])
                fname = img_list[l].split('.')
                fname = fname[0]
                train_fname.append(fname)
        print(train_img)
        print(train_fname)

        # 파일명만 있는것을 확장자(.txt) 붙여서 리스트에 추가하기
        for m in train_fname:
            f_name = m + '.txt'
            train_txt.append(f_name)
        print(train_txt)

        # 이미지 파일들을 저장경로로 이동
        for n in train_img:
            # print(n, type(n))
            src = os.path.join(path, n)
            dst = os.path.join(train_path, n)
            shutil.copyfile(src, dst)

        # 텍스트 파일들을 저장경로로 이동
        for o in train_txt:
            src = os.path.join(path, o)
            dst = os.path.join(train_path, o)
            if os.path.isfile(src):
                shutil.copyfile(src, dst)
            else:
                no_train_txt.append(o)
        print(no_train_txt)



        # 위에서 랜덤으로 가져온 index를 가지고 해당 이미지들을 가져오기 : validation_img
        # 이미지 파일을 파일명만(확장자 제거) 가져오기 : validation_fname
        for p in range(img_list_len):
            if p in validation_num:
                validation_img.append(img_list[p])
                fname = img_list[p].split('.')
                fname = fname[0]
                validation_fname.append(fname)
        print(validation_img)
        print(validation_fname)

        # 파일명만 있는것을 확장자(.txt) 붙여서 리스트에 추가하기
        for q in validation_fname:
            f_name = q + '.txt'
            validation_txt.append(f_name)
        print(validation_txt)

        # 이미지 파일들을 저장경로로 이동
        for r in validation_img:
            src = os.path.join(path, r)
            dst = os.path.join(validation_path, r)
            shutil.copyfile(src, dst)

        # 텍스트 파일들을 저장경로로 이동
        for s in validation_txt:
            src = os.path.join(path, s)
            dst = os.path.join(validation_path, s)
            if os.path.isfile(src):
                shutil.copyfile(src, dst)
            else:
                no_validation_txt.append(s)
        print(no_validation_txt)

    else:         # 디렉토리가 존재하지 않으면
        print('{} 파일 위치 확인 불가'.format(i))
        continue