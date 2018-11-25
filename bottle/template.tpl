<!DOCTYPE html>
<html>
  <head>
    <title>People</title>
  </head>
  <body>
    <table>
      <tr>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Age</th>
        <th>City</th>
      </tr>
      % for p in people:
      <tr>
        <td>{{ p.firstname }}</td>
        <td>{{ p.lastname }}</td>
        <td>{{ p.age }}</td>
        <td>{{ p.city }}</td>
      </tr>
      % end
  </body>
</html>