<script>
  import "../app.css";
</script>

<div class="min-h-screen bg-gray-100 font-sans">
  <header class="bg-white shadow">
    <div class="container mx-auto px-4 py-6">
      <h1 class="text-3xl font-bold text-gray-800">PrepAI</h1>
      <p class="text-gray-600">Your AI-Powered Adaptive Learning Companion</p>
    </div>
  </header>

  <main class="container mx-auto px-4 py-8">
    <slot />
  </main>
</div>
