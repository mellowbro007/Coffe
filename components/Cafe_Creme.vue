<template>
  <div class="Hero container">
    <div class="text-container">
      <h1 class="header"> {{$route.query.cofetype}}</h1>
    </div>
    <img
      class="image"
      src="https://www.cremundo.de/wp-content/uploads/2018/01/nespresso-erfolgsstory.jpg"
      alt= "Cafe Creme konnte nicht geladen werden"
    />

    <v-stepper v-model="position" vertical>
      <template v-for="(item, index) in $route.query.steps">

              <v-stepper-step :complete="position > index + 1" :step="index + 1">
                <h2>
                  {{labels[index +1]}}
                </h2>
              </v-stepper-step>

              <v-stepper-content :step="index+1">
                <router-view></router-view>
              </v-stepper-content>
      </template>
    </v-stepper>

  </div>
</template>

<script>
export default {
  data() {
    return {
      position: 1,
      labels: {
        1:'start', 2: 'start2', 3:'start3', 4:'ende'
      }
    };
  },
  created() {
    this.position=this.$route.query.step
  }
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
