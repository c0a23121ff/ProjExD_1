import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん") #ウィンドウのタイトルを設定
    screen = pg.display.set_mode((800, 600)) #スクリーンの解像度を設定
    clock  = pg.time.Clock() #フレームレート調整用の Clock オブジェクトの生成
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像の読み込み
    koukaton_img = pg.image.load("fig/3.png") #こうかとん画像の読み込み
    koukaton_img = pg.transform.flip(koukaton_img, True, False) #こうかとん画像を左右反転
    bgfl_img = pg.transform.flip(bg_img, True, False) #背景画像を左右反転
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        screen.blit(bg_img, [-x, 0]) #screen surface に背景画像を描画
        screen.blit(bgfl_img, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bgfl_img, [-x+4800, 0])

        screen.blit(koukaton_img, [300, 200]) #screen surface にこうかとん画像を描画

        pg.display.update() #画面を更新
        tmr += 1        
        clock.tick(200) #フレームレートを 200fps に設定


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()