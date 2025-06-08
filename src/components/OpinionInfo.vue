<script setup>
import {ref} from "vue";
import FormInputText from "@/components/FormInputText.vue";
import FormTextArea from "@/components/FormTextArea.vue";
import FormButton from "@/components/FormButton.vue";

const name = ref('')
const message = ref('')

const submitOpinion = () => {
  console.log(name.value)
}
</script>

<template>
  <div class="opinions">
    <div class="content">
      <div class="left">
        <h2>Opinie</h2>
        <p class="intro">
          Opinie naszych uczniów są dla nas najlepszym dowodem skuteczności.
        </p>

        <div class="opinion-list">
          <blockquote>
            „Z EduLeaf zdałem maturę z matematyki! Dziękuję!” – <strong>Mateusz, Gdańsk</strong>
          </blockquote>
          <blockquote>
            „Polubiłam fizykę dzięki świetnym lekcjom online.” – <strong>Klaudia, 17 lat</strong>
          </blockquote>
        </div>
      </div>

      <div class="add-opinion-form">
        <h3>Dodaj swoją opinię</h3>
        <form @submit.prevent="submitOpinion">
          <FormInputText
              :placeholder="'Imię'"
              v-model:input_value="name"
          ></FormInputText>

          <FormTextArea
              :placeholder="'Twoja opinia'"
              v-model:input_value="message"
          ></FormTextArea>

          <FormButton :reset="false">
            <template v-slot:green>
              Wyślij
            </template>
          </FormButton>
        </form>
      </div>
    </div>
  </div>
</template>

<style scoped>
.content {
  width: 90%;
  height: auto;
  margin: 0 auto;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
}

.opinions {
  width: 100%;
  height: auto;
  margin: 0 auto;
  border-top: 2px solid #10b981;
  border-bottom: 2px solid #10b981;
  transition: all 0.3s ease;
  font-size: 1.25vw;
  padding-top: 1rem;
  padding-bottom: 1rem;
  background: linear-gradient(to bottom, #f0fdf4, #ffffff);
}

.left {
  width: 40%;
}

.intro {
  margin-bottom: 2rem;
  color: #334155;
  text-align: center;
}

.opinion-list blockquote {
  font-style: italic;
  border-left: 4px solid #10b981;
  padding: 0.5rem 1rem;
  margin: 1rem 0;
  background: #ecfdf5;
  border-radius: 6px;
}

.add-opinion-form {
  width: 40%;
  padding: 1rem;
  height: auto;
  margin-top: 2rem;
  background-color: #ffffff;
  border-radius: 0.5rem;
  box-shadow: 0 0 4px rgba(0,0,0,0.05);
}

h2 {
  text-align: center;
}

.add-opinion-form h3 {
  margin-bottom: 0.5rem;
  color: #065f46;
}

.add-opinion-form input, .add-opinion-form textarea {
  font-size: 1.25vw;
  width: 80%;
  padding: 0.5rem;
  margin-bottom: 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
}

.add-opinion-form button {
  font-size: 1.15rem;
}
</style>