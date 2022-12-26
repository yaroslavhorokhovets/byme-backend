class URI:
    PING = "/ping"

    class ACCOUNT:
        LOGIN = "/login"
        REGISTER = "/register"
        DETAIL = "/account"
        RANDOM_CHOICE_IMAGE_UPLOAD = "/random-choice-image-upload"

        UPDATE_ACCOUNT = "/account/{account_id}"

        RESET_PASSWORD = "/reset-password"

        ACCOUNT_FILTER = '/account/actions/filter'
        DELETE_ACCOUNT = '/account/actions/delete'
        ACCOUNT_DOWNLOAD_CSV = "/account/actions/download-csv"

    class CATEGORY:
        CATEGORY_DEFAULT = "/category-default"

        CHILD_FILTER_IMAGE = "/{root_category_id}/child/actions/filter/image"
        LST_SUB_CHILD_CATEGORY = "/{root_category_id}/sub-child-category"

        CATEGORY = "/category"

        FILTER_CATEGORY = "/actions/filter/category"

        DETAIL_CATEGORY = "/category/{category_id}"

        SEEN_TUTORIAL_CATEGORY = "/seen/tutorial"

    class BUSINESS:
        BUSINESS_ACCOUNTS = "/business/accounts"
        BUSINESS_STORE_ACCOUNTS = "/business/store"
        BUSINESS_GET_ACCOUNTS = "/business/get"
        BUSINESS_CLOSE_ACCOUNTS = "/business/close"
        BUSINESS_DELETE_ACCOUNTS = "/business/delete"
        BUSINESS_UPLOAD_IMAGES = "/business/upload"

    class TYPE_CATEGORY:
        TYPE_CATEGORY_DEFAULT = "/type-category-default"

        TYPE_CATEGORY = '/type-category'

    class PHOTOGRAPHY_STYLE:
        PHOTOGRAPHY_STYLE_DEFAULT = "/photography-style-default"
        PHOTOGRAPHY_STYLE = "/photography-style"

    class FILE:
        UPLOAD_IMAGE = "/upload/image"
        DOWNLOAD_IMAGE = "/download/image"

        OVERRIDE_IMAGE = "/override/image"

        UPLOAD_FILE = "/upload/file"

        DELETE_FILE_TUTORIAL = "/file/tutorial/action/delete"
        UPLOAD_FILE_TUTORIAL = "/file/tutorial"
        LIST_FILE_TUTORIAL = "/file/tutorial"

        COUNT_FILES_UPLOAD = "/count/files/upload"

        IMAGE_REQUEST_EDIT = "/image/request/edit"

        IMAGE_ACTIONS_DELETE = "/image/actions/delete"

        IMAGE_ACTIONS_FILTER = "/image/actions/filter"

        HISTORY_REQUEST_IMAGE = "/image/request/history"

    class EMAIL:
        SEND_EMAIL_RESET_PASSWORD = "/email/send-mail-reset-password"

    class REPORT:
        REPORT = "/report"
        REPORT_ADMIN = "/report-admin"

    class QUESTION:
        QUESTIONS = "/questions"

    class REQUEST_MEETING:
        REQUEST_MEETING = "/request-meeting"

    class INVOICE:
        UPLOAD_INVOICE = "/upload/invoices"
        DOWNLOAD_INVOICE = "/download/invoices"
        INVOICES = "/invoices"
        INVOICE_DETAIL = "/invoice/{invoice_id}"

        DOWNLOAD_INVOICE_USER = "/download/invoices/user"

    class HISTORY:
        ACTIVITY_HISTORY = "/activity/history"

    class TERMS_OF_USE_AND_PRIVACY_POLICY:
        TERMS_OF_USE = "/terms_of_use"
        PRIVACY_POLICY = "/privacy_policy"

    class PUSH_NOTIFICATION:
        PUSH_NOTIFICATION_EMAIL = "/push/notification/email"
        PUSH_NOTIFICATION_EMAIL_DETAIL = "/push/notification/email/{push_id}"
        PUSH_NOTIFICATION_WEB = "/push/notification/web"
        PUSH_NOTIFICATION_WEB_DETAIL = "/push/notification/web/{push_id}"

    class NOTIFICATION_ACCOUNT:
        LST_NOTIFICATION_ACCOUNT = "/notification/account"

    class RANGE_TAKE_PHOTO:
        OUT = "/out/range"
