<html><title>Spoof 'em all</title>
<h1>Expected Input</h1>
<p>Name: Ozetta</p>
<p>Age: 29</p>
<p>Gender: Ozetta</p>
<p>Interested in: M and F</p>
<p>Email: N/A</p>
<p>Date of birth: Yesterday</p>
<p>Hidden field: No One Plays</p> 

<hr />

<h1>Your Input</h1>
<form method="POST">
<p>Name: <input name="name" type="text" maxlength="5" /></p>
<p>Age: <input name="age" type="range" min="1" max="100" value="50" /> 50 </p>
<p>Gender: <select name="gender"><option value="Male">Male</option><option value="Female">Female</option><option value="Other">Other</option></select></p>
<p>Interested in: <input name="interest[]" type="radio" value="M" /> M <input name="interest[]" type="radio" value="F" /> F </p>
<p>Email: <input name="email" type="email" pattern=".+@ust.hk" /></p>
<p>Date of birth: <input name="dob" type="date" />
<p>Hidden field: <input name="hidden" type="hidden" /></p>
<input name="submit" type="submit" />
</form>

