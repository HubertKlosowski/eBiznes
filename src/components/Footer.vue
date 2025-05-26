<script setup>

</script>

<template>
  <div class="footer">
    <div class="contact">
      <div class="text">
        <h3>Kontakt</h3>
        <p>Adres mail: kontakt@eduleaf.pl</p>
        <p>Numer telefonu: 666-555-888</p>
        <h4>Lokalizacja</h4>
        <p>ul. Radwańska 321, 91-111 Łódź</p>
      </div>
    </div>
    <div class="social_media">
      <h3>Media społecznościowe</h3>
      <a href="https://www.facebook.com/?lsrc=lb">
        <font-awesome-icon :icon="['fab', 'facebook']" class="link" />
        Facebook
      </a>
      <a href="https://x.com/">
        <font-awesome-icon :icon="['fab', 'x-twitter']" class="link" />
        X
      </a>
      <a href="https://discord.com/">
        <font-awesome-icon :icon="['fab', 'discord']" class="link" />
        Discord
      </a>
    </div>
  </div>
</template>

<style scoped>
a {
  width: 30%;
  text-decoration: none;
  color: black;
  font-weight: bold;
  display: flex;
  flex-direction: row;
  align-items: center;
  text-align: center;
}

.contact {
  width: 30%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.social_media {
  width: 30%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.link {
  width: 15%;
  height: 15%;
}

.footer {
  width: 100%;
  height: 50%;
  display: flex;
  flex-direction: row;
  align-items: stretch;
  justify-content: space-evenly;
  margin: 0 auto;
  background-color: #ffffff;
  border-top: 2px solid #10b981;
  border-bottom: 2px solid #10b981;
  transition: all 0.3s ease;
}

.footer > * {
  height: 100%;
  margin: 3rem 1.5rem;
  padding: 0.75rem 1rem;
  background-color: #ecfdf5;
  border-left: 4px solid #10b981;
  border-radius: 6px;
  transition: background-color 0.2s ease;
  justify-content: space-between;
}

.footer > *:hover {
  background-color: #d1fae5;
}
</style>