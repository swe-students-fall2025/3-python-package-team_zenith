import pytest

from pylloween.bat import draw_bat
import pylloween.draw_rand as draw_rand_mod
from pylloween.draw_rand import draw_random, draw_ghost, draw_pumpkin


'''
test for drawing bat
'''

def test_draw_bat_prints(capsys):
    draw_bat()
    out = capsys.readouterr().out
    assert out.strip()                  # non-empty
    assert "/" in out and "\\" in out   # bat wings

"""
test for random drawing function
"""
PUMPKIN_STYLES = {
    1: """
                                    ;::;;::;,
                                    ;::;;::;;,
                                   ;;:::;;::;;,
                   .vnmmnv%vnmnv%,.;;;:::;;::;;,  .,vnmnv%vnmnv,
                vnmmmnv%vnmmmnv%vnmmnv%;;;;;;;%nmmmnv%vnmmnv%vnmmnv
              vnmmnv%vnmmmmmnv%vnmmmmmnv%;:;%nmmmmmmnv%vnmmmnv%vnmmmnv
             vnmmnv%vnmmmmmnv%vnmmmmmmmmnv%vnmmmmmmmmnv%vnmmmnv%vnmmmnv
            vnmmnv%vnmmmmmnv%vnmmmmmmmmnv%vnmmmmmmmmmmnv%vnmmmnv%vnmmmnv
           vnmmnv%vnmmmmmnv%vnmm;mmmmmmnv%vnmmmmmmmm;mmnv%vnmmmnv%vnmmmnv,
          vnmmnv%vnmmmmmnv%vnmm;' mmmmmnv%vnmmmmmmm;' mmnv%vnmmmnv%vnmmmnv
          vnmmnv%vnmmmmmnv%vn;;    mmmmnv%vnmmmmmm;;    nv%vnmmmmnv%vnmmmnv
         vnmmnv%vnmmmmmmnv%v;;      mmmnv%vnmmmmm;;      v%vnmmmmmnv%vnmmmnv
         vnmmnv%vnmmmmmmnv%vnmmmmmmmmm;;       mmmmmmmmmnv%vnmmmmmmnv%vnmmmnv
         vnmmnv%vnmmmmmmnv%vnmmmmmmmmmm;;     mmmmmmmmmmnv%vnmmmmmmnv%vnmmmnv
         vnmmnv%vnmmmmm nv%vnmmmmmmmmmmnv;, mmmmmmmmmmmmnv%vn;mmmmmnv%vnmmmnv
         vnmmnv%vnmmmmm  nv%vnmmmmmmmmmnv%;nmmmmmmmmmmmnv%vn; mmmmmnv%vnmmmnv
         `vnmmnv%vnmmmm,  v%vnmmmmmmmmmmnv%vnmmmmmmmmmmnv%v;  mmmmnv%vnnmmnv'
          vnmmnv%vnmmmm;,   %vnmmmmmmmmmnv%vnmmmmmmmmmnv%;'   mmmnv%vnmmmmnv
           vnmmnv%vnmmmm;;,   nmmm;'              mmmm;;'    mmmnv%vnmmmmnv'
           `vnmmnv%vnmmmmm;;,.         mmnv%v;,            mmmmnv%vnmmmmnv'
            `vnmmnv%vnmmmmmmnv%vnmmmmmmmmnv%vnmmmmmmnv%vnmmmmmnv%vnmmmmnv'
              `vnmvn%vnmmmmmmnv%vnmmmmmmmnv%vnmmmmmnv%vnmmmmmnv%vnmmmnv'
                  `vn%vnmmmmmmn%:%vnmnmmmmnv%vnmmmnv%:%vnmmnv%vnmnv'
    """,
    2: """
                            @@@
                             @@@
                              @@@                       H A P P Y
                              @@@
                      @@@@@@@@@@@@@@@@@@@@@@         H A L L O W E E N
                    @@@@@@@@@@@@@@@@@@@@@@@@@@
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                @@@@@@@@ @@@@@@@@@@@@@@@@ @@@@@@@@
              @@@@@@@@@   @@@@@@@@@@@@@@   @@@@@@@@@
            @@@@@@@@@@     @@@@@@@@@@@@     @@@@@@@@@@
           @@@@@@@@@@       @@@@  @@@@       @@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
           @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@
            @@@@@@@@  @@ @@ @@ @@ @@ @@ @@ @  @@@@@@@@
              @@@@@@@                        @@@@@@@
                @@@@@@  @@ @@ @@ @@ @@ @@ @ @@@@@@
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@
                      @@@@@@@@@@@@@@@@@@@@@@
    """,
    3:r"""
           @@@@
             @@
           @@@@@@
         @@@@@@@@
     @@@@@@@@@@@@
     @@@@@@@@@@@@
     @@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@
     @@@@/@@@@@@@@@@@@
   @@@@@@@@@@@@@\@@@@@
   @@@@@@  @@@@  @@@@@
   @@@@@@  @@@@  @@@@@
   @@::::::@@@@::::::@
   @@::::::@@@@::::::@
   @@@@@@@@@@@@@@@@@@@
   @@@@@@@@@  @@@@@@@@
   @@@@@@@@@   @@@@@@@                    ******
   @@@@@@@@@   @@@@@@@@@                  ******
       @@@@@@@@@@@@@@@@@@@                ******
           @@@@@@@@@@@@@@@@@@ <<<<<<<<<<>>>>>**
             @@@@@@@@@@@@@@ <<<<<<<<<<<<>>>>>>>>>>>>>>>
             @@@@@@@@@@@@ <<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
           @@@@@@@@@@@@@@ <<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>
           @@@@@@@@@@@@ <<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>
         @@@@@@@@@@@@ <<<<<<<<<<<    <<<<>>>>    >>>>>>>>>>>>>>
         @@@@@@@@@@@@ <<<<<<<<        <<<>>>        >>>>>>>>>>>>>
         @@@@@@@@   <<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>
         @@@@@@@@@@ <<<<<<<<<<<<<<<<<<<<  >>>>>>>>>>>>>>>>>>>>>>>>>>
       @@@@@@@@@@@@@@@@<<<<<<<<<<<<<<<      >>>>>>>>>>>>>>>>>>>>>>>
       @@@@@@@@@@@@@@@@@@<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>
       @@@@@@@@@@@@@@@@@@@@<<<   <<<<<<<<>>>>>>>     >>>>>>>>>>>>>
         @@@@@@@@@@@@@@@@@@<<<      <<      >>     >>>>>>>>>>>>>>>
           @@@@@@@@@@@@@@@@<<<                     >>>>>>>>>>>>>>>
             @@@@@@@@@@@@<<<<<<<        <>         >>>>>>>>>>>>>>>
               @@@@@@@@@@<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>
                           <<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>
""",
    4:r"""
                                           ,---._
                                        ,~~,-._  `._
                                         v'~   `-.  `.
                                              _,- ~.  \
                                            .'  ,--`.  `\_
                                            V-'~ ,'~~~`-. `-.
                                ___             /_/~~~) ` `. `._
                       ____,---'   ;            V     `.__ `--, `;
                        `-._    ;  `.                ____)       :
                            `.;  ; .'              ,'        _    |
                             ; |   ;              ,';'~~~`--' `;  :
                            ,': .-'               `,'  __ __   :  |
                            )_  `-, ___     __        (__:__)   ; ;
                       _,---. \___,'` ~`---;  `-.       |||    ;  ;
                   _,-/   :;     !   `     `|    `-.   |~~~~|   ; :
               _,-' /~   .,'  ;  !!  `..    ``.    `.  :    ;  | :
             ,'  ,-'    .;   `; !!   _,'-' ,--._    ====\__/===: `.
           .'  ,-'   ,--.  ~~`-. !!  ~    ,'    `     `./  \   |  |
          .'  :;   ,'    \        !: .   ;--.__   `;.  |. ~.|   : ;
         .'  ,;    ' ,-'~~`-.     ,!  ;-'     #;   `;. \____/  : `.
        .'  ,;      /__      `-._,'!!( _(0'~~`-'    `;.  `.     ; ;
       .'  ,;    ,'    `---._(0))  !! ~   _,-,        `;  `.   ;  :
       ;  ,;    ,' ;;-.__,-._~~~   !!__,--::::|.      `;:  :   `; )
       ;  :|   ,'  ;/;;; :::;;;;----'|:: |::;\/#.      `;  |    ) ;
       :  |:  ,'  ,' :/  :;; \/))):;;::/  ::' ##:      ;;  ;    ; |
       |  :|  :;  :      `'    \/ \/ `'   `'  ##;      ;  .'  ,'  ;
       :  |;  || .'        ;\.   ____ __,--._ ##;     ;' .'--'   ;
   _,--`. `.  :: `./;   /\/;:;,-'    `-.     `--.__     .'~   ,'~
  /     ;. `; ``. :::;\;.-'~~`./~~\/\ ..    _  :::  --. ' ,-'~
 /    .  `. `; `   ~~~ ;~      ~~~~~~`--.__~~`-. :::   ) ~
/'    ;`--`. `. `.    :;      `;       ;   `---`._    ,'
`.  \/      `-.` `_,_ `:,-'-. `.      :_,_    ;   `--'
 `.  `.        ` (___)-: ( ) :--,-'- -(___),'~~~`.
  {_  `.               `.___.' ( ; ;)      :((:)):
    `.  `                       `--'       `.___.'
      `. `.                 ;;:::;
       `-  `.              ;;;. .;
         `-. `.__        \\;;; - ;; //
            `. ` `--..___ \\,--v-, //
              `--._   ~~~~~`)____(//
                   )    ~~   ~~~~~~;
                   `.    ~~  ------;
                    `.~~_   ______,'
                     `. `.--';: |:
                      ;  `. Cc; Cc
                      `.  ;  __
                       `. `-'  ~\
                        `-.__,--'~
    """
}

GHOST_STYLES = {
    1: """
      ⣴⣿⣿⣿⣦
    ⣰⣿⡟⢻⣿⡟⢻⣧
   ⣰⣿⣿⣇⣸⣿⣇⣸⣿
  ⣴⣿⣿⣿⣿⠟⢻⣿⣿⣿
⣠⣾⣿⣿⣿⣿⣿⣤⣼⣿⣿⠇
⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠀
 ⠈⠿⠿⠋⠙⢿⣿⡿⠁
""",
    2: """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠁⠀⠿⢿⣿⡿⣿⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⣿⠃⠀⠿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠋⠁⣿⠟⣿⣿⢿⣧⣤⣴⣿⡇⠀
⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠘⠁⢸⠟⢻⣿⡿⠀⠀
⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣇⢀⣤⠀⠀⠀⠀⠘⣿⠃⠀⠀
⠀⠀⠀⠀⠀⢈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⢀⣴⣾⠇⠀⠀⠀
⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
⠀⠀⠉⠉⠉⠉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⣴⡾⠿⠿⠿⠛⠋⠉⠀⢸⣿⣿⣿⣿⠿⠋⢸⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠟⠋⠁⠀⠀⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""",
    3: """
⠀⠀⠄⠀⠀⠂⠀⠀⠀⡀⠀⠀
⠁⠀⠀⣠⣶⣿⣷⣶⣄⠀⠀⠁
⠈⠀⢰⡿⠛⢿⡿⠻⣿⡆⠀⡀
⠀⠠⣾⡇⠀⢸⡇⠀⢸⣧⠀⠀
⠀⠀⣿⣷⣤⣿⣷⣤⣿⣿⠀⠀
⠠⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⡀
⠄⡀⠙⠟⢿⣿⡿⠿⠿⠋⠀⠀
"""
}


def test_draw_random_pumpkin(monkeypatch, capsys):
  monkeypatch.setattr(draw_rand_mod.random, "randint", lambda a, b: 2)
  draw_random()
  out = capsys.readouterr().out.strip()
  PUMPKIN_SET = {s.strip() for s in PUMPKIN_STYLES.values()}
  assert out.strip() in PUMPKIN_SET
def test_draw_random_ghost(monkeypatch, capsys):
    # 1 -> ghost
    monkeypatch.setattr(draw_rand_mod.random, "randint", lambda a, b: 1)
    draw_random()
    out = capsys.readouterr().out.strip()
    GHOST_SET = {s.strip() for s in GHOST_STYLES.values()}
    assert out.strip() in GHOST_SET

def test_draw_random_picks_bat(monkeypatch, capsys):
    monkeypatch.setattr(draw_rand_mod.random, "randint", lambda a, b: 3)
    draw_random()
    out = capsys.readouterr().out
    assert "/" in out and "\\" in out
