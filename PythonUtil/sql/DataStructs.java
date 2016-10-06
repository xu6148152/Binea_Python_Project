package com.zepp.golfsense.data.models;


import android.net.Uri;
import android.provider.BaseColumns;


public class DataStructs {

	public static final String AUTHORITY = "com.zepp.golfsense.data.models.DataStructs";
	public static final String CONTENT_TYPE = "vnd.android.cursor.dir/vnd.zepp.golfsense";
	public static final String CONTENT_ITEM_TYPE = "vnd.android.cursor.item/vnd.zepp.golfsense";

	// this class cannot be instantiatized
	private DataStructs() {
	}

/* Table name: my_racquet */
public static final class My_racquetColumns implements BaseColumns {
public static final String TABLE_NAME = "my_racquet";
public static final String CONTENT_BOX = "content://" + AUTHORITY + "/"
    				+ TABLE_NAME;
    		public static final Uri CONTENT_URI = Uri.parse(CONTENT_BOX);
    		public static final String CONTENT_TYPE = "vnd.android.cursor.dir/vnd.zepp.golfsense."
    				+ TABLE_NAME;
    		public static final String CONTENT_ITEM_TYPE = "vnd.android.cursor.item/vnd.zepp.golfsense."
    				+ TABLE_NAME;
public static final String "_ID" = ""_id"";
public static final String "MAKE_ID" = ""Make_ID"";
public static final String "MODEL_ID" = ""Model_ID"";
public static final String "MAKE_NAME" = ""Make_Name"";
public static final String "MODEL_NAME" = ""Model_Name"";
public static final String "TYPE_1" = ""Type_1"";
public static final String "TYPE_2" = ""Type_2"";
public static final String "LENGTH" = ""Length"";
public static final String "ICON" = ""Icon"";
public static final String DEFAULT_SORT_ORDER = "_id asc";
public static final String[] PROJECTION = new String[] {_ID, "MAKE_ID", "MODEL_ID", "MAKE_NAME", "MODEL_NAME", "TYPE_1", "TYPE_2", "LENGTH", "ICON" };

}

}

