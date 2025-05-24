<script setup>
import {onMounted, ref} from "vue";

const show_info = ref(0)

const changeTeacher = () => {
  show_info.value === 2 ? show_info.value = 0 : show_info.value += 1
}

onMounted(() => {
  setInterval(changeTeacher, 2000)
})
</script>

<template>
  <div class="teachers">
    <h2>Nasi nauczyciele</h2>
    <p class="intro">
      Nasi nauczyciele to zespół doświadczonych i zaangażowanych edukatorów, którzy z pasją przekazują wiedzę.
      Każdy z nich posiada odpowiednie kwalifikacje, a wielu z nich to egzaminatorzy, nauczyciele akademiccy lub native speakerzy.
      Dzięki nowoczesnym metodom nauczania i indywidualnemu podejściu do ucznia, potrafią skutecznie wspierać rozwój kompetencji oraz przygotowanie do egzaminów.
      W EduLeaf stawiamy na jakość, dlatego każdy nauczyciel przechodzi proces rekrutacji i weryfikacji umiejętności, by zagwarantować najwyższy poziom nauki.
    </p>
    <div class="random_people">
      <div class="person" v-if="show_info === 0">
        <div class="img">
          <img src="@/assets/teacher1.jpg" alt="Katarzyna">
        </div>
        <div class="desc">
          Kasia to entuzjastyczna nauczycielka języka polskiego, która potrafi zarazić pasją do literatury nawet najbardziej opornych uczniów.
          Ukończyła filologię polską na Uniwersytecie Jagiellońskim i od ponad 5 lat pracuje z młodzieżą, przygotowując ją do egzaminu ósmoklasisty i matury.
          Jej zajęcia łączą analizę tekstów z rozwijaniem umiejętności pisarskich i kreatywnego myślenia.
          Uczniowie doceniają jej empatyczne podejście, zrozumiały sposób tłumaczenia i atmosferę wsparcia na lekcjach.
        </div>
      </div>
      <div class="person" v-if="show_info === 1">
        <div class="img">
          <img src="@/assets/teacher2.jpg" alt="Walentyna">
        </div>
        <div class="desc">
          Walentyna to energiczna i zaangażowana nauczycielka matematyki z ponad 7-letnim doświadczeniem w pracy z młodzieżą.
          Ukończyła studia matematyczne na Politechnice Wrocławskiej, a swoją pasję do liczb łączy z nowoczesnym podejściem do nauczania.
          Jej uczniowie cenią ją za cierpliwość, świetne tłumaczenie trudnych zagadnień i indywidualne podejście.
          Przygotowuje zarówno do sprawdzianów, jak i matury – podstawowej i rozszerzonej – osiągając bardzo dobre wyniki.
        </div>
      </div>
      <div class="person" v-if="show_info === 2">
        <div class="img">
          <img src="@/assets/teacher3.png" alt="Łukasz">
        </div>
        <div class="desc">
          Łukasz to absolwent germanistyki na Uniwersytecie Warszawskim, od ponad 15 lat uczy języka niemieckiego na poziomach A1–C1.
          Posiada doświadczenie zarówno w pracy z młodzieżą, jak i z dorosłymi. Wieloletni egzaminator TELC i pasjonat kultury niemieckiej.
          Stawia na praktyczne podejście do nauki – dużo mówi po niemiecku, uczy poprzez dialog i autentyczne materiały.
          Uczniowie cenią go za spokój, cierpliwość i poczucie humoru.
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.teachers {
  width: auto;
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
  width: 15rem;
  height: 17rem;
  object-fit: fill;
  display: block;
}

.random_people > .person {
  width: 50%;
  display: flex;
  flex-direction: row;
  text-align: center;
  font-size: 1rem;
  padding: 0.75rem 1rem;
  background-color: #ecfdf5;
  border: 4px solid #10b981;
  border-radius: 6px;
  margin-bottom: 0.75rem;
  transition: background-color 0.2s ease;
}

.random_people .person:hover {
  background-color: #d1fae5;
  cursor: pointer;
}
</style>