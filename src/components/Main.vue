<script setup>
import CoursesInfo from "@/components/CoursesInfo.vue";
import TeachersInfo from "@/components/TeachersInfo.vue";
import Opinions from "@/components/Opinions.vue";
import AboutUs from "@/components/AboutUs.vue";

</script>

<template>
  <div class="header">
    <div class="company">
      <RouterLink to="/">
        <img src="/src/assets/eduleaf.jpg" alt="logo EduLeaf">
      </RouterLink>
    </div>
    <div class="account">
      <RouterLink to="/account">
        <svg id="Layer_1" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" data-name="Layer 1"><path d="m9.414 15.415-2.704 2.727c-.389.392-1.022.395-1.414.006-.393-.389-.395-1.022-.006-1.414l1.718-1.733h-6.008c-.553 0-1-.448-1-1s.447-1 1-1h6.005l-1.715-1.733c-.389-.392-.387-1.025.006-1.414s1.025-.387 1.414.006l2.707 2.73c.375.374.583.876.583 1.411s-.208 1.037-.586 1.415zm14.586-9.794v15.379c0 1.654-1.346 3-3 3h-10c-1.654 0-3-1.346-3-3v-1c0-.552.447-1 1-1s1 .448 1 1v1c0 .551.448 1 1 1h1v-17.999s0 0 0 0c-1.103 0-2 .897-2 2v2c0 .552-.447 1-1 1s-1-.448-1-1v-2c0-2.206 1.794-4 4-4h.561c.237-.407.528-.785.903-1.092.931-.762 2.138-1.068 3.32-.829l3.196.64c2.329.465 4.02 2.527 4.02 4.902zm-6 6.879c0-.828-.672-1.5-1.5-1.5s-1.5.672-1.5 1.5.672 1.5 1.5 1.5 1.5-.672 1.5-1.5z"/></svg>
      </RouterLink>
    </div>
  </div>
  <div class="main">
    <AboutUs></AboutUs>
    <CoursesInfo></CoursesInfo>
    <TeachersInfo></TeachersInfo>
    <Opinions></Opinions>
  </div>
<!--  <div class="footer">-->
<!--    <div class="contact">-->
<!--      <h4>Kontakt</h4>-->
<!--      <p>Adres mail: kontakt@eduleaf.pl</p>-->
<!--      <p>Numer telefonu: 666-555-888</p>-->
<!--      <h4>Lokalizacja</h4>-->
<!--      <p>ul. Radwańska 321, 91-111 Łódź</p>-->
<!--    </div>-->
<!--    <div class="career">-->
<!--      <h4>Kariera</h4>-->
<!--      <p>Dołącz do zespołu</p>-->
<!--    </div>-->
<!--    <div class="social_media">-->
<!--      <h4>Media społecznościowe</h4>-->
<!--      Facebook, Linkedin-->
<!--    </div>-->
<!--    <div class="sponsors">-->
<!--      <h4>Sponsorzy</h4>-->
<!--      <p>RedBull</p>-->
<!--      <p>Harnaś</p>-->
<!--      <p>Uber Eats</p>-->
<!--    </div>-->
<!--  </div>-->
</template>

<style scoped>
.company {
  max-width: 6%;
  height: auto;
}

.account {
  max-width: 5%;
  height: auto;
  object-fit: contain;
  display: block;
}

.account svg {
  width: 100%;
  height: auto;
  object-fit: contain;
  display: block;
  padding: 0.5rem;
  border-radius: 1rem;
  border: 0.25rem solid black;
}

.company img {
  width: 100%;
  height: auto;
  object-fit: contain;
  display: block;
  border-radius: 2.5rem;
  border: 0.25rem solid black;
}

.header {
  width: 100%;
  height: 20rem;
  display: flex;
  background-color: antiquewhite;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
}

.footer {
  font-size: 1rem;
  width: 100%;
  height: 10rem;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.footer > * {
  height: 100%;
  min-width: 5rem;
  width: 20%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: aliceblue;
  border-radius: 2rem;
  padding: 1rem;
  margin: 0.5rem;
  box-shadow: 10px 5px 5px red;
}

.footer > *:hover {
  box-shadow: 10px 5px 5px yellow;
}

.main {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>