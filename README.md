# 🏀 Three Point Focus
### Author: Christian Vaikona

This project uses NBA 3‑point shot tracking data to model players’ shooting hotspots and translate them into optimal baseline positions for sports photographers, showcasing an end‑to‑end Python + SQL + R analytics workflow.

### Tech Stack:

- **Languages**:        `Python` `SQL` `R`
- **Python libraries**: `pandas` `numpy` `scikit-learn` `nba_api`
- **Database**:         `MySQL`
- **R libraries**:      `ggplot2` `DBI`
- **Tooling**:          `Jupyter Notebooks` `Git` `GitHub`

---

As a sports photographer hobbyist, I like to delve into the nitty-gritty details of the craft every now and then. One of these details is positioning. That leads to questions like "Where should I be? Where might be the best spot to get a really strong photo?". 

Let's say I'm at an NBA game. I've been asked to photograph the best 3-point shooters in the game. Now, typically, photographers are only allowed on the baselines of the court, if near the court at all. This simplifies the job, but I want THE optimal spot on the baseline. This project aims to provide just that.

---

**Technically speaking...**

I am taking all data directly related to the players' shooting statistics and filtering shot location coordinates to those outside of the 3-point boundary. Then, splitting by player, I am modelling their statistics, tendencies, and predictions of zones where the player will shoot their 3-point shots from. Results will be used to provide recommendations for photographer's optimal location. For this project, I will narrow down to 5 players among the league’s top 3‑point shooters by attempts and percentage.

---

There are a couple other factors that I, as the photographer, am going to think about when choosing THE optimal spot. One of which is which hand they shoot with, maybe even their entire shooting form. Trivial to some, this makes or breaks a photo. The last thing I want is the player's face to be covered by their arm when shooting. Here are some examples:

![3 images as examples of 3-point shot photos where one is undesireable](figures/README_figures/tpf-readme-fig1.png)

Which photo do you think might make it harder for a viewer to identify the player? 

---

**Technically speaking...**

I incorporate an encoded series indicating whether a player is a left-handed shooter or right-handed. Following the modeling of zones they are likely to shoot from, recommedations for placement of photographers will be emphasized opposite the side of the player's shooting hand from the zone. That is, if the photographer is facing the player, and the player shoots right‑handed, the photographer sits to the right so the face isn’t blocked by the shooting arm.

[Plot Figure Example]

---

Another factor I want to consider when choosing my spot is my equipment, more importantly the focal length and aperture of the lenses I bring to the game. 

*While focal length determines how far a subject can be and remain the same size in a frame, aperture determines the depth of field, how blurry the background of the image will be. The larger the focal length, the further the subject can be, but narrower the field of view, and vice versa. The larger the aperture number (usually preceded by an "f"), meaning a narrower aperture opening, the more in focus the background will be and vice versa.*

For sports, the ideal aperture is f2.8 (Larger aperture opening with blurrier background) and I will assume this ideal for this project. The standard focal length in sports photography is a 70-200mm lens. This is generally optimal for about a 6-30 yard reach. However, I also want to curate some photos with a variety in perspective as the pictures show. When I can understand where the player will most likely shoot from, I can start to think about and plan some photos I think will be pretty cool and choose the best equipment and locations for those photos, stepping out of what may be THE optimal location to photograph the player at all.

![3 images as examples of photos taken at different focal lengths](figures/README_figures/tpf-readme-fig2.png)

The following standard practice specs and ranges assume the subject is in the same position:

| Standard Lens Specifications | Approximate Range From Subject |
|------------------------------|--------------------------------|
| 24-70mm f2.8                 | 3-12 yards                     |
| 70-200mm f2.8                | 6-30 yards                     |
| 300mm f2.8                   | 18-45 yards                    |
| 400mm f2.8                   | 25-65 yards                    |

---

**Technically speaking...**

I will have predetermined an axis parallel to the baseline of the court along which the positioning of the photographer will generally be (Media zones are typically determined by league officials). Following the modeling of zones the players are likely to shoot from, I will calculate the average distance between predicted shot zones and candidate photographer positions as well as calculate other options for a photographer for each lens option in the table. I will discretize this into groups using the yard ranges as bins.

---

With this tool in hand, a photographer on a similar assignment can be much more intentional about where to sit and what to bring.

I give you **Three Point Focus**.