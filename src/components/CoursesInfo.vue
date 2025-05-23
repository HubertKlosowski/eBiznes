<script setup>
// komponent statyczny, nie wymaga logiki setup na razie
</script>

<template>
  <section class="courses">
    <h2>Nasze kursy</h2>
    <p class="intro">
      Oferujemy szeroki wybór kursów online dostosowanych do różnych poziomów nauczania. Nasi doświadczeni nauczyciele pomagają uczniom zrozumieć trudne zagadnienia, przygotować się do sprawdzianów i egzaminów oraz rozwijać pasję do nauki.
    </p>

    <div class="course-list">
      <span><strong>Matematyka:</strong> Kursy od podstawówki po maturę. Zrozumienie zasad, praktyka, egzaminy.</span>
      <span><strong>Język angielski:</strong> Gramatyka, słownictwo, konwersacje, certyfikaty językowe.</span>
      <span><strong>Język niemiecki:</strong> Lekcje z native speakerami. Mówienie, pisanie, czytanie.</span>
      <span><strong>Język polski:</strong> Przygotowanie do egzaminów, wypracowania, lektury.</span>
      <span><strong>Fizyka:</strong> Zrozumiałe wyjaśnienia zjawisk, teoria i zadania.</span>
      <span><strong>Chemia:</strong> Reakcje, równania, przygotowanie do egzaminów.</span>
    </div>
  </section>
</template>

<style scoped>
.courses {
  width: 100%;
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

.course-list {
  display: flex;
  flex-direction: column;
  padding: 0;
  color: #1f2937;
}

.course-list span {
  padding: 0.75rem 1rem;
  background-color: #ecfdf5;
  border-left: 4px solid #10b981;
  border-radius: 6px;
  margin-bottom: 0.75rem;
  transition: background-color 0.2s ease;
}

.course-list span:hover {
  background-color: #d1fae5;
}
</style>
