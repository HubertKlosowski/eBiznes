<script setup>

</script>

<template>
  <div class="about_us">
    <h2>O nas</h2>
    <p class="intro">
      EduLeaf to nowoczesna platforma edukacyjna oferująca korepetycje i kursy online dla uczniów szkół podstawowych i średnich.
      Łączymy najlepszych nauczycieli z technologią, aby zapewnić efektywną i elastyczną naukę.
    </p>
    <div class="more">
      <div class="x">
        Profesjonalizm
      </div>
      <div class="x">
        Dokładność
      </div>
      <div class="x">
        Rzetelność
      </div>
    </div>
  </div>
</template>

<style scoped>
.about_us {
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

.more {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
  padding: 0;
  color: #1f2937;
}

.more > .x {
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

.more .x:hover {
  background-color: #d1fae5;
}
</style>