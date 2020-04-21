def compare():
    # 获取数据并转为列表
    version1 = input()
    version2 = input()
    versionListOne = version1.split('.')
    versionListTwo = version2.split('.')

    # 计算出最大和最小的比较次数
    if len(versionListOne) >= len(versionListTwo):
        max_compare_count = len(versionListOne)
        min_compare_count = len(versionListTwo)
    else:
        max_compare_count = len(versionListTwo)
        min_compare_count = len(versionListOne)

    # 如果列表长度一样可以比到最后
    if len(versionListOne) == len(versionListTwo):
        for i in range(max_compare_count):
            if int(versionListOne[i]) > int(versionListTwo[i]):
                return 1
                break
            elif int(versionListOne[i]) < int(versionListTwo[i]):
                return -1
                break
            else:  # 比到最后
                if i == max_compare_count - 1:
                    return 0

    # 列表长度不一样
    else:
        # 循环短列表判断大小
        for i in range(min_compare_count):
            if int(versionListOne[i]) > int(versionListTwo[i]):
                return 1
                break
            elif int(versionListOne[i]) < int(versionListTwo[i]):
                return -1
                break
            else:
                # 如果短列表循环之后无法判断时，计算长列表后半段数值和
                if i == min_compare_count - 1:

                    # 版本1长列表长时
                    if len(versionListOne) > len(versionListTwo):
                        num = 0
                        for j in versionListOne[i:]:
                            num += int(j)
                        if num > 0:
                            return 1
                        else:
                            return 0

                    # 版本2列表长时
                    if len(versionListOne) < len(versionListTwo):
                        num = 0
                        for j in versionListTwo[i:]:
                            num += int(j)
                        if num > 0:
                            return -1
                        else:
                            return 0


if '__main__' == __name__:
    while True:
        print(compare())
