<script setup>

</script>

<template>
  <div class="footer">
    <div class="contact">
      <h4>Kontakt</h4>
      <p>Adres mail: kontakt@eduleaf.pl</p>
      <p>Numer telefonu: 666-555-888</p>
      <h4>Lokalizacja</h4>
      <p>ul. Radwańska 321, 91-111 Łódź</p>
    </div>
    <div class="career">
      <h4>Kariera</h4>
      <p>Dołącz do zespołu</p>
    </div>
    <div class="social_media">
      <h4>Media społecznościowe</h4>
      Facebook, Linkedin
    </div>
    <div class="sponsors">
      <h4>Sponsorzy</h4>
      <p>RedBull</p>
      <p>Harnaś</p>
      <p>Uber Eats</p>
    </div>
  </div>
</template>

<style scoped>
.footer {
  font-size: 1rem;
  width: 100%;
  min-height: 10rem;
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
}
</style>