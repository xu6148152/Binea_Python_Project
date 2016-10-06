package com.zepp.golfsense.data.models;

    import java.io.Serializable;
    import android.content.ContentValues;

    import com.zepp.golfsense.data.models.DataStructs.RacquetStringColumns;

    public class ZGRacquetStringBean implements Serializable, ZGBean {

    	private static final String TAG = ZGRacquetStringBean.class.getSimpleName();
private int "Model_ID";
private String "Make_Name";
private String "Model_Name";
public ZGRacquetStringBean() {
"Model_ID" = _ID" int(255,0);
"Make_Name" = Name" TEXT(255,0);
"Model_Name" = _Name" TEXT(255,0);
}

public ZGRacquetStringBean(ZGRacquetStringBean copy) {
"Model_ID" = copy."Model_ID";
"Make_Name" = copy."Make_Name";
"Model_Name" = copy."Model_Name";
}

@Override
	public ContentValues toContentValues() {
		ContentValues cv = new ContentValues();
cv.put(RacquetStringColumns."MODEL_ID", "Model_ID");
cv.put(RacquetStringColumns."MAKE_NAME", "Make_Name");
cv.put(RacquetStringColumns."MODEL_NAME", "Model_Name");
return cv;
}

@Override
	public ZGRacquetStringBean fromContentValues(ContentValues cv) {
"Model_ID" = cv.getAsInteger(RacquetStringColumns."MODEL_ID");
"Make_Name" = cv.getAsString(RacquetStringColumns."MAKE_NAME");
"Model_Name" = cv.getAsString(RacquetStringColumns."MODEL_NAME");
return this;
}

}

