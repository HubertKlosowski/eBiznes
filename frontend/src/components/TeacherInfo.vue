<script setup>
import {onMounted, ref, watch} from "vue";

const counter = ref(0)
const pause = ref(false)

const teachers = ref([
  {
    name: 'Katarzyna',
    img: new URL('@/assets/teacher1.jpg', import.meta.url).href,
    small_desc: 'Katarzyna. Nauczyciel języka polskiego',
    desc: 'Kasia to entuzjastyczna nauczycielka języka polskiego, która potrafi zarazić pasją do literatury nawet najbardziej opornych uczniów.\n' +
        '          Ukończyła filologię polską na Uniwersytecie Jagiellońskim i od ponad 5 lat pracuje z młodzieżą, przygotowując ją do egzaminu ósmoklasisty i matury.\n' +
        '          Jej zajęcia łączą analizę tekstów z rozwijaniem umiejętności pisarskich i kreatywnego myślenia.\n' +
        '          Uczniowie doceniają jej empatyczne podejście, zrozumiały sposób tłumaczenia i atmosferę wsparcia na lekcjach.'
  },
  {
    name: 'Walentyna',
    img: new URL('@/assets/teacher2.jpg', import.meta.url).href,
    small_desc: 'Walentyna. Nauczyciel matematyki',
    desc: 'Walentyna to energiczna i zaangażowana nauczycielka matematyki z ponad 7-letnim doświadczeniem w pracy z młodzieżą.\n' +
        '          Ukończyła studia matematyczne na Politechnice Wrocławskiej, a swoją pasję do liczb łączy z nowoczesnym podejściem do nauczania.\n' +
        '          Jej uczniowie cenią ją za cierpliwość, świetne tłumaczenie trudnych zagadnień i indywidualne podejście.\n' +
        '          Przygotowuje zarówno do sprawdzianów, jak i matury – podstawowej i rozszerzonej – osiągając bardzo dobre wyniki.'
  },
  {
    name: 'Łukasz',
    img: new URL('@/assets/teacher3.png', import.meta.url).href,
    small_desc: 'Łukasz. Nauczyciel języka niemieckiego',
    desc: 'Łukasz to absolwent germanistyki na Uniwersytecie Warszawskim, od ponad 15 lat uczy języka niemieckiego na poziomach A1–C1.\n' +
        '          Posiada doświadczenie zarówno w pracy z młodzieżą, jak i z dorosłymi. Wieloletni egzaminator TELC i pasjonat kultury niemieckiej.\n' +
        '          Stawia na praktyczne podejście do nauki – dużo mówi po niemiecku, uczy poprzez dialog i autentyczne materiały.\n' +
        '          Uczniowie cenią go za spokój, cierpliwość i poczucie humoru.'
  }
])

let active_pearson = null

onMounted(() => {
  active_pearson = setInterval(() => {
    counter.value = (counter.value + 1) % teachers.value.length
  }, 2000)
})

watch(counter, () => {
  const first = teachers.value.shift()
  teachers.value.push(first)
})

watch(pause, () => {
  if (pause.value === true) {
    clearInterval(active_pearson)
  } else {
    active_pearson = setInterval(() => {
      counter.value = (counter.value + 1) % teachers.value.length
    }, 2000)
  }
})
</script>

<template>
  <div class="teachers">
    <div class="content">
      <h2>Nasi nauczyciele</h2>
      <p class="intro">
        Nasi nauczyciele to zespół doświadczonych i zaangażowanych edukatorów, którzy z pasją przekazują wiedzę.
        Każdy z nich posiada odpowiednie kwalifikacje, a wielu z nich to egzaminatorzy, nauczyciele akademiccy lub native speakerzy.
        Dzięki nowoczesnym metodom nauczania i indywidualnemu podejściu do ucznia, potrafią skutecznie wspierać rozwój kompetencji oraz przygotowanie do egzaminów.
        W EduLeaf stawiamy na jakość, dlatego każdy nauczyciel przechodzi proces rekrutacji i weryfikacji umiejętności, by zagwarantować najwyższy poziom nauki.
      </p>
      <div class="random_people">
        <div :class="i === 1 ? 'active_person' : 'person'" v-for="(el, i) in teachers" :key="el">
          <div class="img">
            <img :src="el.img" :alt="el.name">
          </div>
          <div class="small_desc">
            <b>{{ el.small_desc }}</b>
          </div>
          <div class="desc" v-if="pause && i === 1">
            {{ el.desc }}
          </div>
          <div class="link" v-if="i === 1" @click="pause = !pause">
            <font-awesome-icon :icon="['fas', 'play']" v-if="pause" />
            <font-awesome-icon :icon="['fas', 'pause']" v-else />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.desc {
  width: 90%;
  text-align: justify;
  background-color: #065f46;
  color: #ecfdf5;
  border-radius: 0.5rem;
  padding: 0.75rem 1rem;
  margin-top: 1rem;
  line-height: 1.6;
}

.content {
  width: 90%;
  height: auto;
  margin: 0 auto;
}

.link {
  width: 10%;
  padding: 0;
  font-size: 1.5vw;
}

.teachers {
  width: 100%;
  min-height: 45vh;
  margin: 0 auto;
  border-top: 2px solid #10b981;
  border-bottom: 2px solid #10b981;
  transition: all 0.3s ease;
  font-size: 1.25vw;
  background: linear-gradient(to bottom, #f0fdf4, #ffffff);
}

h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #065f46;
  text-align: center;
}

.intro {
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
  margin-top: 5rem;
  margin-bottom: 3rem;
  color: #1f2937;
}

.img img {
  width: 100%;
  height: 17rem;
  object-fit: fill;
  display: block;
}

.person, .active_person {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  font-size: 1rem;
  padding: 0.75rem 1rem;
  background-color: #ecfdf5;
  border: 4px solid #10b981;
  border-radius: 6px;
  margin-bottom: 0.75rem;
  transition: background-color 0.2s ease;
  cursor: pointer;
}

.person {
  width: 50%;
  opacity: 0.4;
  transition: all 0.2s ease;
}

.active_person {
  width: 70%;
  opacity: 1;
  z-index: 1;
  transform: scale(1.1);
}

.person:hover {
  background-color: #d1fae5;
  cursor: pointer;
}
</style>