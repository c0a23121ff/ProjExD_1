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
    koukaton_rct = koukaton_img.get_rect()
    koukaton_rct.center = [300, 200]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        screen.blit(bg_img, [-x, 0]) #screen surface に背景画像を描画
        screen.blit(bgfl_img, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bgfl_img, [-x+4800, 0])
        key_lst = pg.key.get_pressed() #キー入力を key_lst に格納
        if key_lst[pg.K_UP]:
            koukaton_rct.move_ip(0, -1)
        if key_lst[pg.K_DOWN]:
            koukaton_rct.move_ip(0, 1)
        if key_lst[pg.K_LEFT]:
            koukaton_rct.move_ip(-1, 0)
        if key_lst[pg.K_RIGHT]:
            koukaton_rct.move_ip(1, 0)
        screen.blit(koukaton_img, koukaton_rct) #screen surface にこうかとん画像を描画

        pg.display.update() #画面を更新
        tmr += 1        
        clock.tick(200) #フレームレートを 200fps に設定


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()