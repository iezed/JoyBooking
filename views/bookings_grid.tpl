% rebase('base.tpl', title=title)

<div class="container mt-5">
  <h1 class="mb-4">Bookings</h1>
    <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">Client Name</th>
            <th scope="col">Client Phone</th>
            <th scope="col">Slot</th>
          </tr>
        </thead>
        <tbody>
            % for booking in bookings:
            <tr>
                <td>{{ booking['client_name'] }}</td>
                <td>{{ booking['client_phone'] }}</td>
                <td>{{ booking['slot'] }}</td>
            </tr>
            % end
        </tbody>
    </table>

    <nav aria-label="Page navigation">
        <ul class="pagination justify-content-center">
            <li class="page-item {{ 'disabled' if current_page == 1 else '' }}">
                <a class="page-link" href="/bookings?page={{ current_page - 1 }}" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                </a>
            </li>
            % for i in range(1, total_pages + 1):
            <li class="page-item {{ 'active' if i == current_page else '' }}">
                <a class="page-link" href="/bookings?page={{ i }}">{{ i }}</a>
            </li>
            % end
            <li class="page-item {{ 'disabled' if current_page == total_pages else '' }}">
                <a class="page-link" href="/bookings?page={{ current_page + 1 }}" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                </a>
            </li>
        </ul>
    </nav>
</div>