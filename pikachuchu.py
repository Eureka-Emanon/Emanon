#!/usr/bin/env python3
'''
This script is for displaying a Pikachu animation with text in your terminal
Please Enjoy it
'''
import os
import time
import datetime

# 皮卡丘动画帧
def get_pikachu_frames():
    frames = []
    # 帧1
    frame1 = [
        "     $$         $   ",
        "    $/$        $l$  ",
        "    $l$       $lll$ ",
        "   $ll$    $$$llll$ ",
        "   $ll$  $$//$lll$  ",
        "  $llll$$ll/$lll$   ",
        " $lllllllll$$ll$    ",
        "$Clllllllll$llll$   ",
        "$$lllllllll$ll$l$   ",
        "$llllC$lllll$$l$    ",
        " $lll$$BBlll$$$     ",
        "  $llllBlll$$$      ",
        " $llllllllllL$      ",
        "  $$lllll$lll$      ",
        "   $llll$lllL$      ",
        "  $l$llll$lll$      ",
        "  $$$$$lllll$       ",
        "       $$$l$$       ",
        "        $lll$       ",
        #"         $$$        "
    ]
    frames.append(frame1)
    # 帧2
    frame2 = [
        "                    ",
        "     $$        $    ",
        "    $/$   $   $l$   ",
        "    $l$  $/$ $lll$  ",
        "   $ll$  $/$$llll$  ",
        "   $ll$ $ll$$lll$   ",
        "  $llll$$ll$$ll$    ",
        " $lllllllll$$l$     ",
        "$Clllllllll$l$      ",
        "$$lllllllll$ll$     ",
        "$llllC$lllll$l$     ",
        " $lll$$BBlll$$$     ",
        " $lllllBlll$L$      ",
        "  $$lllll$lll$      ",
        "   $llll$lllL$      ",
        "  $l$llll$lll$      ",
        "  $$$$$lllll$       ",
        "       $$$l$$       ",
        "        $lll$       ",
        #"         $$$        "
    ]
    frames.append(frame2)
    # 帧3（与帧1相同）
    frames.append(frame1)
    # 帧4（优化）
    frame4 = [
        "    $         $$    ",
        "   $l$        $/$   ",
        "  $lll$       $l$   ",
        "  $llll$$$    $ll$  ",
        "   $lll$//$$  $ll$  ",
        "    $lll$/ll$$llll$ ",
        "     $ll$$lllllllll$",
        "    $llll$lllllllllC",
        "    $l$ll$lllllllll$",
        "     $l$$lllll$Clll$",
        "      $$$lllBB$$ll$ ",
        "       $$$lllBllll$ ",
        "       $Lllllllllll$",
        "       $lll$lllll$$ ",
        "       $Llll$llll$  ",
        "       $lll$llll$l$ ",
        "        $lllll$$$$$ ",
        "        $$l$$$      ",
        "        $lll$       ",
        #"         $$$        "
    ]
    frames.append(frame4)
    # 帧5（优化）
    frame5 = [
        "                    ",
        "    $        $$     ",
        "   $l$   $   $/$    ",
        "  $lll$ $/$  $l$    ",
        "  $llll$$/$  $ll$   ",
        "   $lll$$ll$ $ll$   ",
        "    $ll$$ll$$llll$  ",
        "     $l$$lllllllll$ ",
        "      $l$lllllllllC ",
        "     $ll$lllllllll$ ",
        "     $l$lllll$Clll$ ",
        "     $$$lllBB$$ll$  ",
        "      $L$lllBllll$  ",
        "      $lll$lllll$$  ",
        "      $Llll$llll$   ",
        "      $lll$llll$l$  ",
        "       $lllll$$$$$  ",
        "       $$l$$$       ",
        "       $lll$        ",
        #"        $$$         "
    ]
    frames.append(frame5)
    # 帧6（与帧4相同）
    frames.append(frame4)
    return frames

# 获取皮卡丘动画帧
Pika_frames = get_pikachu_frames()

# 颜色映射
Pika_pattern = {
    " ":"  ",
    "$$":"\x1b[30;3;6m\u2588\x1b[0m",
    "$/":'\x1b[0;40;2m\u2584\x1b[0m',
    "/$":'\x1b[0;40;2m\u2580\x1b[0m',
    "$C":'\x1b[0;40;6m\u2584\x1b[0m',
    "C$":'\x1b[0;40;6m\u2580\x1b[0m',
    "$L":'\x1b[30;100;6m\u2580\x1b[0m',
    "L$":'\x1b[30;100;6m\u2584\x1b[0m',
    "//":'\x1b[30;0;2m\u2588\x1b[0m',
    "BB":'\x1b[31;3;6m\u2588\x1b[0m',
    " l":'\x1b[33;33;6m\u2584\x1b[0m',
    "l ":'\x1b[33;33;6m\u2580\x1b[0m',
    " $":"\x1b[30;3;6m\u2584\x1b[0m",
    "$ ":"\x1b[30;3;6m\u2580\x1b[0m",
    " /":'\x1b[30;0;2m\u2584\x1b[0m',
    "/ ":'\x1b[30;0;2m\u2580\x1b[0m',
    "ll":'\x1b[33;40;6m\u2588\x1b[0m',
    "l$":'\x1b[33;40;6m\u2580\x1b[0m',
    "$l":'\x1b[33;40;6m\u2584\x1b[0m',
    "l/":'\x1b[0;43;2m\u2584\x1b[0m',
    "/l":'\x1b[0;43;2m\u2580\x1b[0m',
    "lB":'\x1b[33;41;6m\u2580\x1b[0m',
    "Bl":'\x1b[33;41;6m\u2584\x1b[0m',
    "lC":'\x1b[0;43;6m\u2584\x1b[0m',
    "Cl":'\x1b[0;43;6m\u2580\x1b[0m',
    "lL":'\x1b[33;100;6m\u2580\x1b[0m',
    "Ll":'\x1b[33;100;6m\u2584\x1b[0m'
}

# 文本字符艺术
MIDDLE_TEXT = "皇军托Pikachu给您带句话:\n"
HELLO_TEXT = [
    [
    "H   H EEEEE L     L     OOOOO",
    "H   H E     L     L     O   O",
    "HHHHH EEEEE L     L     O   O",
    "H   H E     L     L     O   O",
    "H   H EEEEE LLLLL LLLLL OOOOO",
    "                             ",
    "PPPP  SSSS Y   Y DDDD  U   U  CCC  K   K",
    "P   P S      Y   D   D U   U C     K  K ",
    "PPPP  SSSS   Y   D   D U   U C     KKK  ",
    "P        S   Y   D   D U   U C     K  K ",
    "P     SSSS   Y   DDDD   UUU   CCC  K   K"
    ],
    [
    "\n",
    "\n",
    "H   H EEEEE L     L     L     OOOOO",
    "H   H E     L     L     L     O   O",
    "HHHHH EEEEE L     L     L     O   O",
    "H   H E     L     L     L     O   O",
    "H   H EEEEE LLLLL LLLLL LLLLL OOOOO",
    "\n"
    ]
]

'''
L_PSYDUCK_TEXT =[
     [
    "PPPP  SSSS Y   Y DDDD  U   U  CCC  K   K",
    "P   P S      Y   D   D U   U C     K  K ",
    "PPPP  SSSS   Y   D   D U   U C     KKK  ",
    "P        S   Y   D   D U   U C     K  K ",
    "P     SSSS   Y   DDDD   UUU   CCC  K   K"
],
[
    "  L",
    "  L",
    "  L",
    "  L",
    "   LLL"
    ]
]
'''
# 不同时间段的文本
TIME_BASED_TEXTS = {
    7: "嗯嗯",
    10: "HELLO",
    13: "Pikachu想告诉你们",
    16: "一个冷知识",
    19: "如果你们冷暴力Pikachu",
    22: "它就会变成",
    28: "直流Pikachu",
    31: "不通交流",
    34: "......",
    40: "Nothing more. Good night",
    50: "你可以继续等待,",
    55: "至少这还有一只Pikachu(别嫌它丑)",
    #120: "...",
    #123: "HELLO?",
    #128: ""
}

def display_text(text_lines, color_code='\x1b[1;37;40m'):
    """显示文本"""
    for line in text_lines:
        colored_line = color_code + line + '\x1b[0m'
        # 居中对齐 - 使用皮卡丘动画的宽度
        padding = (max(len(line) for line in Pika_frames[0]) * 2 - len(line)) // 2
        print(" " * padding + colored_line)

def display_middle_text(text, color_code='\x1b[1;31;40m'):
    """显示中间文本（不居中）"""
    colored_text = color_code + text + '\x1b[0m'
    print(colored_text)

def display_center_text(text, color_code='\x1b[1;37;40m'):
    """居中显示文本"""
    colored_text = color_code + text + '\x1b[0m'
    # 居中对齐 - 使用皮卡丘动画的宽度
    padding = (max(len(line) for line in Pika_frames[0]) * 2 - len(text)) // 2
    print(" " * padding + colored_text)

def render_pikachu(frame):
    """渲染皮卡丘动画帧"""
    result = ""
    for i in range(0, len(frame), 2):
        if i + 1 >= len(frame):
            break
            
        line_top = frame[i]
        line_bottom = frame[i+1]
        
        # 确保两行长度相同
        max_len = max(len(line_top), len(line_bottom))
        line_top = line_top.ljust(max_len, ' ')
        line_bottom = line_bottom.ljust(max_len, ' ')
        
        # 组合上下两行
        for j in range(max_len):
            pair = line_top[j] + line_bottom[j]
            if pair in Pika_pattern:
                result += Pika_pattern[pair]
            else:
                result += "  "  # 默认空格
        
        result += "\n"
    
    return result

def get_time_based_text(elapsed_time):
    """根据经过的时间获取相应的文本"""
    for time_threshold in sorted(TIME_BASED_TEXTS.keys(), reverse=True):
        if elapsed_time >= time_threshold:
            return TIME_BASED_TEXTS[time_threshold]
    return "稍等"

L_index = 0
frame_index = 0
start_time = time.time()
cnt=0
A=1

while A:
    if cnt<=60:
        if (cnt>=34):
            L_index = 1
        else:
            L_index = 0
        # 清屏
        os.system("cls" if os.name == "nt" else "clear")
    
        # 计算经过的时间
        elapsed_time = int(time.time() - start_time)
    
    

    
    # 显示皮卡丘动画当前帧
        animation = render_pikachu(Pika_frames[frame_index])
        print(animation)
    
    # 显示中间文本（在皮卡丘下方，不居中）
        display_middle_text(MIDDLE_TEXT, '\x1b[1;31;40m')  # 红色文本
    
    # 显示HELLO文本
        display_text(HELLO_TEXT[L_index], '\x1b[1;33;40m')  # 黄色文本
    
    # 显示PSYDUCK文本
        #display_text(L_PSYDUCK_TEXT[L_index], '\x1b[1;36;40m')  # 青色文本
    
    # 显示时间信息（居中）
        time_text = f"\n感谢你驻足了{elapsed_time}秒:"
        display_center_text(time_text, '\x1b[1;37;40m')  # 白色文本
        print()  # 空行
    
    # 显示基于时间的文本（居中）
        time_based_text = get_time_based_text(elapsed_time)
        display_center_text(time_based_text, '\x1b[1;31;40m')  # 红色文本
    
        time.sleep(1)
    
    #L_index = (L_index + 1) % len(L_PSYDUCK_TEXT)
        frame_index = (frame_index + 1) % len(Pika_frames)
        cnt+=1
    elif(60<cnt<90):
        cnt+=1
        time.sleep(1)
    elif(cnt==90):
        cnt+=1
        print("120 seconds passed...")
        time.sleep(1)
    elif(120>cnt>90) :
        cnt+=1
        time.sleep(1)
    elif(cnt>=120):
        print("\nIt's been 3 minutes.")
        #print("\nThat suit,matches up pretty...")
        #time.sleep(3)
        #print("\nPretty.Not only form the view of a \"producer\".")
        #time.sleep(3)
        #print("\n--Seems like I had said some similar words before.\n\nBut what matters is that")
        #time.sleep(3)
        #print("\nmaybe u don't like this kind of words?")
        #time.sleep(3) 
        #print("\nSorry.After all,sometimes I am just good at ...")
        #time.sleep(3)
        #print("\nmaking situations embarrassing.")
        #time.sleep(3)
        #print("\nWhatever,the most important is that, trust me,I didn't mean to make a remark,")
        #print("so called \"评头论足\" in Chinese.")
        time.sleep(3)
        print("\nWhen I talked about your suit,")
        time.sleep(3)
        print("\ntrust me, I Didn't mean to make a remark,")
        time.sleep(3)
        print("\nlike so called \"评头论足\" in Chinese,sorry.")
        time.sleep(5)
        print("\nAnyway,I said too much,so just stop here.")
        time.sleep(3)
        print("\n参考资料: https://github.com/Karobben/Karobben-Work-Station/blob/master")
        time.sleep(3)
        print("\n源码: https://github.com/Eureka-Emanon/Emanon")
        time.sleep(3)
        print("\n\n---Life is short,I use Python---")
        A=0

time.sleep(24*3600)  # 休眠24小时
print("\nA century's wait is too short.A day's pursuit is too long.\n")

# Thanks for getting here.




