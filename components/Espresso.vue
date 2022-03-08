<template>
  <div class="Hero container">
    <div class="text-container">
      <h1 class="header">Espresso</h1>
    </div>
    <img
      class="image"
      src="https://image.brigitte.de/10115348/t/sn/v8/w1440/r1.7778/-/espresso-eckig.jpg"
      alt="Espresso konnte nicht geladen werden"
    />

    <div class="stepper">
      <v-stepper alt-labels>
        <v-stepper-header>
          <v-stepper-step step="1"> Step 1 </v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step step="2"> Step 2 </v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step step="3"> Step 3 </v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step step="3"> Finish </v-stepper-step>
        </v-stepper-header>
      </v-stepper>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      e1: 1,
    };
  },
};
</script>

<style scoped>
.image {
  justify-content: center;
  width: 27.5rem;
  margin-top: 2rem;
  margin-block-end: 30px;
}
.header {
  font-weight: 900;
  font-size: 5rem;
  margin-block-end: -20px;
  margin-top: 5px;
}
</style>
