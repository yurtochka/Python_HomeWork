import view
import model
import text_fields as txt


def start_pb():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.load_file()
                view.print_info(txt.load_successful)
            case 2:
                model.save_file()
                view.print_info(txt.save_successful)
            case 3:
                pb = model.get_pb()
                view.show_contacts(pb, txt.no_contact_or_file)
            case 4:
                contact = view.new_contact()
                model.add_contact(contact)
                view.print_info(txt.new_contact_successful)
            case 5:
                item_search = view.search_contacts()
                item = model.search_data(item_search)
                view.print_info(txt.res_search)
                view.show_contacts(item, txt.no_data_search)
            case 6:
                pb = model.get_pb()
                xxx = view.show_contacts(pb, txt.no_contact_or_file)
                number_contact_change = view.number_change_book()
                if number_contact_change > xxx:
                    view.print_info(txt.no_contact)
                else:
                    contact = view.new_contact()
                    model.change_contact(number_contact_change, contact)
                    model.del_contact(number_contact_change)
                    view.print_info(txt.add_change_cont)
            case 7:
                pb = model.get_pb()
                view.show_contacts(pb, txt.no_contact_or_file)
                num_contact = view.del_contact()
                model.del_contact(num_contact)
                view.print_info(txt.cont_was_del)
            case 8:
                if model.exit_pb():
                    if view.confirm(txt.is_changed):
                        model.save_file()
                view.print_info(txt.bye_bye)
                exit()
