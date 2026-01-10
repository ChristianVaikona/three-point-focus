# Three Point Focus
### Author: Christian Vaikona

This project uses NBA 3‑point tracking data to model players’ shooting hotspots and translate them into optimal baseline positions for sports photographers, showcasing an end‑to‑end Python + SQL + R analytics workflow

### Tech Stack:

[Bullet points? Just list? ... ]

---

As a sports photographer hobbyist, I like to delve into the nitty-gritty details of the craft every now and then. One of these details is positioning. This detail leads to questions like "Where should I be? Where might be the best spot for me to get a really cool picture?". 

Let's say I'm at an NBA game. I've been asked to photograph the best 3-point shooters in the game. Now, typically, photographers are only allowed on the baselines of the court, if near the court at all. This simplifies the job, but I want THE optimal spot on the baseline. This project aims to provide just that.

---

### Technical speaking...

I am taking all data directly related to the players' 3-point shooting, also filtering shot location coordinates to those outside of the 3-point boundary, and by player, modeling statistics, tendencies, and predicitions of zones where the player will shoot their 3-point shots from

---

There are a few other factors that I, as the photographer, am going to think about when choosing THE optimal spot. One of which is which hand they shoot with, maybe even their entire shooting form. Trivial to some, this makes or breaks a photo. The last thing I want is the player's face to be covered by their arm when shooting. Here are some examples:

![3 images as examples of 3-point shot photos where one is undesireable](figures/README_figures/tpf-readme-fig1.png)

Which photo do you think might make it harder for a viewer to identify the player? 

---

### Technically speaking...

I incorporate an encoded series indicating whether a player is a left-handed shooter or right-handed. Following the modeling of zones they are likely to shoot from, recommmedations for placement of photographers will be emphasized opposite the side of the player's shooting arm from the zone (ie. Facing the player, if the player shoots right-handed, the photographer will move to the right of the player's shooting zone)

---