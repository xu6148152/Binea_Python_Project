package com.zepp.golfsense.data.models;

    import java.io.Serializable;
    import android.content.ContentValues;

    import com.zepp.golfsense.data.models.DataStructs.RacquetTensionColumns;

    public class ZGRacquetTensionBean implements Serializable, ZGBean {

    	private static final String TAG = ZGRacquetTensionBean.class.getSimpleName();
private String "Tension";
public ZGRacquetTensionBean() {
"Tension" = on" TEXT(255,0);
}

public ZGRacquetTensionBean(ZGRacquetTensionBean copy) {
"Tension" = copy."Tension";
}

@Override
	public ContentValues toContentValues() {
		ContentValues cv = new ContentValues();
cv.put(RacquetTensionColumns."TENSION", "Tension");
return cv;
}

@Override
	public ZGRacquetTensionBean fromContentValues(ContentValues cv) {
"Tension" = cv.getAsString(RacquetTensionColumns."TENSION");
return this;
}

}

