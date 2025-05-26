<script setup>
import {ref} from "vue";
import Footer from "@/components/Footer.vue";
import Header from "@/components/Header.vue";

const questions = ref([
  {
    q: "Jak zapisać się na kurs?",
    a: "Aby zapisać się na kurs, wybierz interesujący Cię temat i kliknij przycisk 'Zapisz się'. Zostaniesz przekierowany do formularza rejestracyjnego."
  },
  {
    q: "Czy muszę płacić z góry za cały kurs?",
    a: "Tak, płatność za cały kurs jest wymagana przed rozpoczęciem zajęć. Umożliwia to rezerwację miejsca i dostęp do materiałów."
  },
  {
    q: "Jakie są metody płatności?",
    a: "Akceptujemy płatności przelewem bankowym, kartą płatniczą oraz przez systemy płatności online, takie jak PayU i Blik."
  },
  {
    q: "Czy otrzymam fakturę lub potwierdzenie płatności?",
    a: "Tak, po zaksięgowaniu płatności otrzymasz e-mail z fakturą VAT lub potwierdzeniem opłaty."
  },
  {
    q: "Czy mogę zrezygnować z kursu i otrzymać zwrot pieniędzy?",
    a: "Możesz zrezygnować do 3 dni przed rozpoczęciem kursu – wtedy przysługuje pełny zwrot. Po tym terminie zwroty nie są możliwe."
  },
  {
    q: "Ile osób maksymalnie może brać udział w kursie?",
    a: "Maksymalna liczba uczestników zależy od kursu, ale zazwyczaj mieści się w przedziale od 10 do 20 osób, aby zapewnić indywidualne podejście."
  },
  {
    q: "Czy są dostępne kursy online?",
    a: "Tak, większość kursów dostępna jest zarówno w wersji stacjonarnej, jak i online. Informacja o formie znajduje się w opisie kursu."
  },
  {
    q: "Czy mogę uzyskać certyfikat po ukończeniu kursu?",
    a: "Tak, po ukończeniu kursu uczestnicy otrzymują certyfikat potwierdzający zdobyte umiejętności."
  },
  {
    q: "Czy poziomy kursów są dostosowane do wiedzy uczestników?",
    a: "Tak, kursy są podzielone na poziomy: początkujący, średniozaawansowany i zaawansowany, aby każdy mógł znaleźć coś dla siebie."
  },
  {
    q: "Jak długo trwa jeden kurs?",
    a: "Długość kursów różni się w zależności od tematyki – od 20 do 40 godzin lekcyjnych. Szczegóły znajdziesz w opisie konkretnego kursu."
  }
])
const show_info = ref(-1)
</script>

<template>
  <div class="contact">
    <Header></Header>
    <div class="frequently-asked">
      <h2>Często zadawane pytania</h2>
      <div class="questions">
        <div class="row" v-for="(qa, i) in questions" :key="qa">
          <div class="q">
            <span><b>Pytanie: </b>{{ qa.q }}</span>
            <font-awesome-icon :icon="['fas', 'arrow-up']" class="link" @click="show_info = -1" v-if="show_info === i" />
            <font-awesome-icon :icon="['fas', 'arrow-down']" class="link" @click="show_info = i" v-else />
          </div>
          <div class="a" v-if="show_info === i">
            <span><b>Odpowiedź: </b>{{ qa.a }}</span>
          </div>
        </div>
      </div>
    </div>
    <Footer :reuse="true"></Footer>
  </div>
</template>

<style scoped>
.link {
  width: 2%;
  padding: 0.5rem;
  text-align: center;
  align-content: center;
}

.frequently-asked {
  width: 100%;
  margin: 0 auto;
  border-top: 2px solid #10b981;
  border-bottom: 2px solid #10b981;
}

.frequently-asked h2 {
  font-size: 2rem;
  margin-bottom: 1.5rem;
  text-align: center;
  color: #111827;
}

.questions {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 100%;
}

.row {
  background-color: #f9fafb;
  transition: background-color 0.3s;
  align-items: center;
}

.row:hover {
  background-color: #f0fdf4;
}

.q {
  font-weight: 600;
  height: 50%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
}

.a {
  height: 50%;
  padding: 1rem 1rem 1.5rem 1rem;
  background-color: #ecfdf5;
  border-top: 2px solid black;
  font-weight: 400;
  line-height: 1.6;
}

.contact {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  min-height: 100vh;
  width: 100%;
}
</style>