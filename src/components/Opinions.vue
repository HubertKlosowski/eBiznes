<script setup>

</script>

<template>
  <div class="opinions">
    <h2>Opinie</h2>
    <p class="intro">
      Opinie naszych uczniów są dla nas najlepszym dowodem skuteczności.
      Cieszymy się, że dzięki EduLeaf wielu z nich osiąga lepsze wyniki, odzyskuje motywację do nauki i zyskuje pewność siebie przed egzaminami.
    </p>
    <div class="more">
      <div class="add_opinion">
        <form>
          <textarea>Tekst</textarea>
          <button type="submit">Wyślij</button>
        </form>
      </div>
      <div class="random_opinions">

      </div>
    </div>
  </div>
</template>

<style scoped>
.opinions {
  width: 100%;
  height: auto;
  margin: 0 auto;
  padding: 3rem 1.5rem;
  background-color: #ffffff;
  border-top: 2px solid #10b981;
  border-bottom: 2px solid #10b981;
  transition: all 0.3s ease;
}

h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #065f46;
  text-align: center;
}

.intro {
  font-size: 1.1rem;
  color: #374151;
  margin-bottom: 1.5rem;
  line-height: 1.6;
  text-align: center;
}

.random_people {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
  padding: 0;
  color: #1f2937;
}

.img img {
  width: 100%;
  height: auto;
  object-fit: contain;
  display: block;
}

.random_people > .person {
  width: 20%;
  text-align: center;
  font-size: 1rem;
  font-weight: bold;
  padding: 0.75rem 1rem;
  background-color: #ecfdf5;
  border: 4px solid #10b981;
  border-radius: 6px;
  margin-bottom: 0.75rem;
  transition: background-color 0.2s ease;
}

.random_people .person:hover {
  background-color: #d1fae5;
}
</style>