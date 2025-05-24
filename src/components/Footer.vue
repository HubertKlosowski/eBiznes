<script setup>

</script>

<template>
  <div class="footer">
    <div class="contact">
      <h3>Kontakt</h3>
      <p>Adres mail: kontakt@eduleaf.pl</p>
      <p>Numer telefonu: 666-555-888</p>
      <h4>Lokalizacja</h4>
      <p>ul. Radwańska 321, 91-111 Łódź</p>
    </div>
    <div class="career">
      <h3>Kariera</h3>
      <p>Dołącz do zespołu</p>
    </div>
    <div class="social_media">
      <h3>Media społecznościowe</h3>
      <p>Facebook</p>
      <p>Linkedin</p>
    </div>
    <div class="sponsors">
      <h3>Sponsorzy</h3>
      <p>RedBull</p>
      <p>Harnaś</p>
      <p>Uber Eats</p>
    </div>
  </div>
</template>

<style scoped>
.footer {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
  margin: 0 auto;
  background-color: #ffffff;
  border-top: 2px solid #10b981;
  border-bottom: 2px solid #10b981;
  transition: all 0.3s ease;
}

.footer > * {
  margin: 3rem 1.5rem;
  padding: 0.75rem 1rem;
  background-color: #ecfdf5;
  border-left: 4px solid #10b981;
  border-radius: 6px;
  transition: background-color 0.2s ease;
}

.footer > *:hover {
  background-color: #d1fae5;
  cursor: pointer;
}
</style>