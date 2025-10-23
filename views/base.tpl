<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
  <title>{{title}}</title>
  <!-- Bootstrap 5 CSS -->
  <link rel="stylesheet" href="/static/css/bootstrap.min.css">
  <link rel="stylesheet" href="/static/css/app.css">
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="/">JoyBooking</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/bookings">Bookings</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<!-- Main Content Section -->
<main>{{!base}}</main>
<!-- Footer Section -->
<!-- Bootstrap 5 JS Bundle -->
<script src="/static/js/bootstrap.bundle.min.js"></script>
</body>
</html>