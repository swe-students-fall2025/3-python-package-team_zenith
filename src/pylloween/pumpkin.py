import random
from typing import Optional, Union

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

def draw_pumpkin(style: Optional[Union[int, str]] = None):
    """
    Prints a Halloween pumpkin (ASCII) to the console.

    Parameters
    ----------
    style : int | str | None, optional
    """
    if style is None:
        chosen = random.choice(list(PUMPKIN_STYLES.keys()))
    else:
        if isinstance(style, str):
            try:
                chosen = int(style)
            except ValueError as exc:
                raise ValueError(
                    "style must be an integer key matching the available pumpkin styles"
                ) from exc
        elif isinstance(style, int):
            chosen = style
        else:
            raise TypeError("style must be an int, str, or None")

        if chosen not in PUMPKIN_STYLES:
            raise ValueError(f"style must be one of {sorted(PUMPKIN_STYLES.keys())}")

    print(PUMPKIN_STYLES[chosen])
