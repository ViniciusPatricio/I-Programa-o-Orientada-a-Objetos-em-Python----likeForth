from like_forth_interpreter import LikeForthInterpreter

quadrado = '''
( ** Quadrado ** )
: sq dup * ;
." Quadrado: " 5 sq .
'''

fatorial = '''
( ** Fatorial ** )
: fat ( n -- n! )
dup 2 < if
drop 1
else
dup 1 - fat *
then
;
." 5! = " 5 fat .
'''
loops = '''
( ** Loops ** )
." DO..LOOP: " 10 0 do i . loop cr
." BEGIN..UNTIL: " 0 begin 1 + dup . dup 10 eq until
'''

blackjack = '''
( ** Blackjack ** )
: copy2 ( a b -- a b a b ) over over ;
: randint ( a b -- randint(a,b) ) rand + ;
: .n dup . ;
: deal_cards_1 1 10 randint .n ;
: deal_cards_2 deal_cards_1 deal_cards_1 + ;
: ask_card
." -- Quer outra carta (1 = sim, 0 = nao)? "
acceptn
;
: player_guesses
begin
ask_card
1 eq if
." Voce pegou a carta " deal_cards_1
." e tem agora " + .n cr dup
else
." Voce ficou com " .n ." pontos " cr
0
then
dup 21 > if
." Infelizmente, voce passou de 21. "
cr drop 0
then
0 eq until
;
: house_should_guess
( p h -- -1 if p<=21 and h<=21 and h<p else 0 )
dup 
21 
<= 
rot
dup 
21 <=     
rot 
and       
;

: house_guess ( p h -- h' )
dup rot >= if
." A mesa pegou a carta " deal_cards_1
." e tem agora " + .n cr
then
;


: house_guesses ( p h -- p' h' )
begin
." Inicio do Loop" cr
over >r  ( save player score )
copy2  house_should_guess  if
house_guess
( get saved player score
and new house score )
r> swap
-1
else
0
then
." Final do Loop" cr
0 eq until
swap
;


: player_over_21 ( p h -- )
21 > swap 21 < and if ( h>21 and p<21 )
." Voce ganhou!!!! " cr
else
." Voce perdeu. Tente novamente. " cr
then
;
: player_no_21 ( p h -- )
copy2 over 21 < rot > and if ( p<21 and p>h )
." Voce ganhou pq ficou +perto de 21! " cr
else
player_over_21
then
;
: announce_winner ( p h -- )
over 21 eq if ( p == 21 )
." 21!! Voce ganhou! " cr
else
player_no_21
then
;
: blackjack
." ====================================== " cr
." Blackjack (super simples) " cr
." ====================================== " cr
." Cartas da Mesa: " deal_cards_2 ." = " .n cr
>r
." Suas cartas: " deal_cards_2 ." = " .n cr
>r
r> player_guesses
r> house_guesses
announce_winner
;
blackjack
'''

if __name__ == "__main__":

    interpreter = LikeForthInterpreter()
    test_ = True
    if test_:
        interpreter.run(quadrado)
        interpreter.run(fatorial)
        interpreter.run(loops)
        interpreter.run(blackjack)
    else:
        interpreter.run()