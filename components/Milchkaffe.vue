<template>
  <div class="Hero container">
    <div class="text-container">
        <h1 class="header">Milchkaffe</h1>
    </div>
    <img 
    class="image" 
    src="https://media.istockphoto.com/photos/cup-of-latte-coffee-and-spoon-on-gray-counter-picture-id183138035?b=1&k=20&m=183138035&s=170667a&w=0&h=z3mma5Uf5QrKcyVEcaGUjp-d6w9MnMRZ0GlwZ9X8OGU=" 
    alt="Milchkaffe konnte nicht geladen werden">

  <div class="stepper">
    <v-stepper alt-labels>
    <v-stepper-header>
      <v-stepper-step step="1">
        Step 1 
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="2">
        Step 2 
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="3">
        Step 3 
      </v-stepper-step>
    </v-stepper-header>
  </v-stepper>
  </div>
  
  </div>
</template>

<script>
  export default {
    data () {
      return {
        e1: 1,
      }
    },
  }
</script>

<style scoped>
  .header {
      font-weight: 900;
      font-size: 5rem;
      margin-block-end: -20px;
  }
  .image {
      justify-content: center;
      width: 27.5rem;
      margin-top: 2rem;
      margin-block-end: 30px;
  }

  .header {
    margin-top: 5px;
  }

  @media (max-width: 500px) {
      .Hero {
          height: 40vh;
      }
  }
</style>