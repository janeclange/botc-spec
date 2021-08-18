Require Import List ListSet.

Inductive Alignment : Set := 
  | Good
  | Evil. 

Inductive Townsfolk_role : Set := 
  | Washerwoman
  | Librarian
  | Investigator
  | Chef 
  | Empath
  | Fortune_teller
  | Undertaker
  | Monk
  | Ravenkeeper 
  | Virgin 
  | Slayer 
  | Soldier 
  | Mayor.

Inductive Outsider_role : Set := 
  | Butler
  | Drunk
  | Recluse
  | Saint.

Inductive Minion_role : Set := 
  | Poisoner
  | Spy
  | Scarlet_woman
  | Baron.

Inductive Demon_role : Set := 
  | Imp.


Inductive Role : Set := 
  | Townsfolk (r : Townsfolk_role) 
  | Outsider (r : Outsider_role) 
  | Minion (r : Minion_role) 
  | Demon (r : Demon_role).

Inductive Status := 
  | Alive
  | Dead_with_vote
  | Dead_no_vote.

Definition first_night : list Role :=
  Minion Poisoner :: 
  Townsfolk Washerwoman ::
  Townsfolk Librarian ::
  Townsfolk Investigator ::
  Townsfolk Chef ::
  Townsfolk Empath ::
  Townsfolk Fortune_teller ::
  Outsider Butler ::
  Minion Spy :: nil.

Definition other_nights : list Role := 
  Minion Poisoner :: 
  Townsfolk Monk ::
  Minion Scarlet_woman ::
  Demon Imp :: 
  Townsfolk Ravenkeeper ::
  Townsfolk Empath ::
  Townsfolk Fortune_teller ::
  Outsider Butler ::
  Townsfolk Undertaker :: 
  Minion Spy :: nil.

Inductive Phase := 
  | Day 
  | Night (turn : nat).

Record Player := 
  { pos : nat
  ; role : Role
  ; alignment : Alignment
  ; status : Status
  ; info : Prop
  }. 

Record State := 
  { players : list Player
  ; phase : Phase 
  ; ndays : nat
  ; nominated_players : list Player
  ; chopping_block : option Player
  ; unique_roles := forall (p1 p2 : Player), In p1 players -> In p2 players -> role p1 = role p2 -> p1 = p2 
  }.

(* examples *)
Definition p1 := 
  {| pos := 0
   ; role := Townsfolk Washerwoman
   ; alignment := Good
   ; status := Alive
   ; info := True
  |}.

Definition p2 := 
  {| pos := 1
   ; role := Demon Imp
   ; alignment := Evil
   ; status := Alive
   ; info := True
  |}.

Definition s := 
  {| players := p1 :: p2 :: nil
   ; phase := Night 0
   ; ndays := 0
   ; nominated_players := nil 
   ; chopping_block := None 
  |}.

Theorem p1_role : role p1 = Townsfolk Washerwoman.
Proof. constructor. Qed.


Theorem s_alive : forall (p : Player), In p (players s) -> status p = Alive.
Proof. 
  intros.
  destruct H; subst; eauto.
  destruct H; subst; eauto.
  destruct H.
Qed.
 

(* now what? *) 

(*Definition Imp_action (n : nat) (s : State) : State := 
  let target := (
    let target_original := nth_error (players s) n 
   {| pos := pos target_original*)
  
  

