package com.zepp.golfsense.data.models;

    import java.io.Serializable;
    import android.content.ContentValues;

    import com.zepp.golfsense.data.models.DataStructs.ClubsColumns;

    public class ZGClubsBean implements Serializable, ZGBean {

    	private static final String TAG = ZGClubsBean.class.getSimpleName();
private int racquet_make_id;
private int racquet_model_id;
private int mount_type;
private int main_string_make_id;
private int main_string_model_id;
private int main_string_guage;
private int main_string_tension;
private int cross_string_make_id;
private int cross_string_model_id;
private int cross_string_gauge;
private int cross_string_tension;
public ZGClubsBean() {
racquet_make_id = 0;
racquet_model_id = 0;
mount_type = 0;
main_string_make_id = 0;
main_string_model_id = 0;
main_string_guage = 0;
main_string_tension = 0;
cross_string_make_id = 0;
cross_string_model_id = 0;
cross_string_gauge = 0;
cross_string_tension = 0;
}

public ZGClubsBean(ZGClubsBean copy) {
racquet_make_id = copy.racquet_make_id;
racquet_model_id = copy.racquet_model_id;
mount_type = copy.mount_type;
main_string_make_id = copy.main_string_make_id;
main_string_model_id = copy.main_string_model_id;
main_string_guage = copy.main_string_guage;
main_string_tension = copy.main_string_tension;
cross_string_make_id = copy.cross_string_make_id;
cross_string_model_id = copy.cross_string_model_id;
cross_string_gauge = copy.cross_string_gauge;
cross_string_tension = copy.cross_string_tension;
}

@Override
	public ContentValues toContentValues() {
		ContentValues cv = new ContentValues();
cv.put(ClubsColumns.RACQUET_MAKE_ID, racquet_make_id);
cv.put(ClubsColumns.RACQUET_MODEL_ID, racquet_model_id);
cv.put(ClubsColumns.MOUNT_TYPE, mount_type);
cv.put(ClubsColumns.MAIN_STRING_MAKE_ID, main_string_make_id);
cv.put(ClubsColumns.MAIN_STRING_MODEL_ID, main_string_model_id);
cv.put(ClubsColumns.MAIN_STRING_GUAGE, main_string_guage);
cv.put(ClubsColumns.MAIN_STRING_TENSION, main_string_tension);
cv.put(ClubsColumns.CROSS_STRING_MAKE_ID, cross_string_make_id);
cv.put(ClubsColumns.CROSS_STRING_MODEL_ID, cross_string_model_id);
cv.put(ClubsColumns.CROSS_STRING_GAUGE, cross_string_gauge);
cv.put(ClubsColumns.CROSS_STRING_TENSION, cross_string_tension);
return cv;
}

@Override
	public ZGClubsBean fromContentValues(ContentValues cv) {
racquet_make_id = cv.getAsInteger(ClubsColumns.RACQUET_MAKE_ID);
racquet_model_id = cv.getAsInteger(ClubsColumns.RACQUET_MODEL_ID);
mount_type = cv.getAsInteger(ClubsColumns.MOUNT_TYPE);
main_string_make_id = cv.getAsInteger(ClubsColumns.MAIN_STRING_MAKE_ID);
main_string_model_id = cv.getAsInteger(ClubsColumns.MAIN_STRING_MODEL_ID);
main_string_guage = cv.getAsInteger(ClubsColumns.MAIN_STRING_GUAGE);
main_string_tension = cv.getAsInteger(ClubsColumns.MAIN_STRING_TENSION);
cross_string_make_id = cv.getAsInteger(ClubsColumns.CROSS_STRING_MAKE_ID);
cross_string_model_id = cv.getAsInteger(ClubsColumns.CROSS_STRING_MODEL_ID);
cross_string_gauge = cv.getAsInteger(ClubsColumns.CROSS_STRING_GAUGE);
cross_string_tension = cv.getAsInteger(ClubsColumns.CROSS_STRING_TENSION);
return this;
}

}

